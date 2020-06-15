from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from common.decorators import ajax_required
from .form import *
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from actions.utils import create_action
import redis
from django.conf import settings

# Create your views here.
r = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)

@login_required
def image_create(request):
    if request.method == "POST":
        #表单提交
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            #表单通过验证
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #将当前用户附加到数据对象上
            new_item.user = request.user
            new_item.save()
            create_action(request.user,'添加了图片',new_item)
            messages.success(request,'图片添加成功')
            return redirect(new_item.get_absolute_url())
    else:
        #根据GET请求传入的参数建立表单对象
        form = ImageCreateForm(data=request.GET)
    return render(request,'images/image/create.html',{'section':'images','form':form})

def image_detail(request,id,slug):
    image = get_object_or_404(Image,id=id,slug=slug)
    # 浏览数+1
    total_views = r.incr('image:{}:views'.format(image.id))
    # 在有序集合image_ranking里，把image.id的分数增加１
    r.zincrby('image_ranking',image.id,1)
    return render(request,'images/image/detail.html',{'section':'images','image':image,'total_views':total_views})

@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user,'点赞了',image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

@login_required()
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images,8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        #如果页书不是整数，就返回第一页
        images = paginator.page(1)
    except EmptyPage:
        # 如果是不存在的页数，而且请求是AJAX请求，返回空字符串
        if request.is_ajax():
            return HttpResponse('')
        # 如果页数超过范围，显示的是最后一页
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,'images/image/list_ajax.html',{'section':'images','images':images})
    return render(request,'images/image/list.html',{'section':'images','images':images})


@login_required
def image_ranking(request):
    # 获得排名前十的图片ＩＤ列表
    image_ranking = r.zrange('image_ranking',0,-1,desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    # 取排名最高的图片然后排序
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x:image_ranking_ids.index(x.id))
    return render(request,'images/image/ranking.html',{'section':'images','most_viewed':most_viewed})