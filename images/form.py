from urllib import request

from django import forms
from django.core.files.base import ContentFile

from .models import *

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')
        widgets = {
            'url':forms.HiddenInput,
        }
    #图片类型验证
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg','jpeg']
        extensions = url.split('.',1)[1].lower()
        if extensions in valid_extensions:
            raise forms.ValidationError('图片的类型不匹配')
        return url

    #重写save()方法
    def save(self,force_insert=False,force_update=False,commit=True):
        image = super(ImageCreateForm,self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),image_url.split('.',1)[1].lower())

        #根据ＵＲＬ下载图片
        response = request.urlopen(image_url)
        image.image.save(image_name,ContentFile(response.read()),save=False)

        if commit:
            image.save()
        return image

