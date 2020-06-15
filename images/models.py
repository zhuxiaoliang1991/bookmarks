from django.conf import settings
from django.db import models
from django.urls import reverse
from uuslug import slugify

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE,verbose_name='用户')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='images_liked',blank=True,verbose_name='喜欢该图片的用户')
    title = models.CharField(max_length=200,verbose_name='标题')
    slug = models.SlugField(max_length=200,blank=True,verbose_name='标称')
    url = models.URLField(verbose_name='地址')
    image = models.ImageField(upload_to='images/%Y/%m/%d',verbose_name='图片')
    description = models.TextField(blank=True,verbose_name='描述')
    created = models.DateField(auto_now_add=True,db_index=True,verbose_name='创建时间')
    total_like = models.PositiveIntegerField(db_index=True,default=0)


    class Meta:
        db_table='image'
        verbose_name = '图片'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(self,*args,**kwargs)

    def get_absolute_url(self):
        return reverse('images:detail',args=[self.id,self.slug])