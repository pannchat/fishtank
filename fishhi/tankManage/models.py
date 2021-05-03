from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Feed(models.Model):
    id = models.BigAutoField(help_text="Feed ID", primary_key=True)
    title = models.CharField(help_text="Feed title", max_length=100, blank=False, null=False)
    contents = models.TextField(help_text="",blank=True, null=True)
    width = models.IntegerField(help_text="width",blank=True,null=True)
    depth = models.IntegerField(help_text="depth",blank=True,null=True)
    height = models.IntegerField(help_text="height",blank=True,null=True)
    public = models.BooleanField(help_text="공개여부", default=True)
    username = models.ForeignKey(User , on_delete=models.CASCADE, default="admin")
    thumbnail = models.ImageField(upload_to="thumbnail/%Y/%M/%d", null=True,blank=True)
    changewater = models.CharField(help_text="환수요일", null=True,blank=True,max_length=10)
    start = models.DateField(help_text="시작일", null=True, blank=True)
    def __str__(self):
        return self.title

class Fish(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE, default="admin", null=True,blank=True)
    SEX_CHOICE = (
        ('F','암컷'),
        ('M','수컷'),
        ('N','설정안함'),
    )
    id = models.BigAutoField(help_text="fishes ID", primary_key=True)
    feed_fish_id = models.ForeignKey("Feed", related_name="feed_fish", on_delete=models.CASCADE, db_column="feed_fish_id")
    name = models.CharField(help_text="fishes Name", blank=False, null=False,max_length=40)
    img = models.ImageField(upload_to="images/%Y/%m/%d" , null=True, blank=True)
    sex = models.CharField(
        help_text="fishes Sex",
        max_length=1,
        choices=SEX_CHOICE,
        default='N'
    )
    hmf = models.IntegerField(default=0,help_text="마리수")
    get = models.DateField(blank=True, null=True,help_text="입수날짜")
    price =  models.IntegerField(default=0,null=True,blank=True,help_text="가격")
    
    class Meta:
        verbose_name_plural = "Fieshes"
    def __str__(self):
        return self.name
class Plant(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE, default="admin", null=True,blank=True)
    id = models.BigAutoField(help_text="plants ID", primary_key=True)
    feed_plant_id = models.ForeignKey("Feed", related_name="feed_plant", on_delete=models.CASCADE, db_column="feed_plant_id")
    name = models.CharField(help_text="plants Name", blank=False, null=False,max_length=40)
    get = models.DateField(blank=True, null=True,help_text="입수날짜")
    price =  models.IntegerField(default=0,null=True,blank=True,help_text="가격")
    img = models.ImageField(upload_to="images/%Y/%m/%d" , null=True, blank=True)
    def __str__(self):
        return self.name

class Supplies(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE, default="admin", null=True,blank=True)
    id = models.BigAutoField(help_text="supplies ID", primary_key=True)
    img = models.ImageField(upload_to="images/%Y/%m/%d" , null=True, blank=True)
    feed_supplies_id = models.ForeignKey("Feed", related_name="feed_supplies", on_delete=models.CASCADE, db_column="feed_supplies_id")
    name = models.CharField(help_text="supplies Name", blank=False, null=False,max_length=40)
    get = models.DateField(blank=True, null=True,help_text="구매날짜")
    price =  models.IntegerField(default=0,null=True,blank=True,help_text="가격")

    class Meta:
        verbose_name_plural = "Supplies"
    def __str__(self):
        return self.name

class Timeline(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="content_type_timelines", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.CharField(max_length=250, default="created")


