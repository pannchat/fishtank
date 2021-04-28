from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
    nickname = models.CharField(max_length=64, null=True,blank=True)
    profile_photo = models.ImageField(blank=True)                

