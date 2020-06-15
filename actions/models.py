from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class Action(models.Model):
    user = models.ForeignKey('auth.User',related_name='actions',db_index=True,on_delete=models.CASCADE,verbose_name='用户')
    verb = models.CharField(max_length=255,verbose_name='行为描述')
    target_ct = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj',on_delete=models.CASCADE,verbose_name='关联模型')
    target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True,verbose_name='关联模型主键')
    target = GenericForeignKey('target_ct','target_id')
    created = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='动作时间')

    class Meta:
        db_table = 'action'
        verbose_name = '用户行为记录'
        verbose_name_plural = verbose_name
        ordering = ('-created',)