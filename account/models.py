from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile',verbose_name='用户')
    date_of_birth = models.DateField(blank=True,null=True,verbose_name='出生日期')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True,null=True,verbose_name='照片')

    class Meta:
        db_table = 'profile'
        verbose_name = '个人信息'
        verbose_name_plural=verbose_name
    def __str__(self):
        return 'Profile for user()'.format(self.user.username)


class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='rel_from_set',on_delete=models.CASCADE,verbose_name='用户')
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='rel_to_set',on_delete=models.CASCADE,verbose_name='关注的用户')
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    class Meta:
        db_table = 'contact'
        verbose_name = '关注关系'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return '{}关注{}'.format(self.user_from,self.user_to)

User.add_to_class('following',models.ManyToManyField('self',through=Contact,related_name='followers',symmetrical=False))
