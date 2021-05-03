# Generated by Django 3.1.7 on 2021-04-28 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(help_text='Feed ID', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Feed title', max_length=100)),
                ('contents', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField(default=True, help_text='공개여부')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/%Y/%M/%d')),
                ('changewater', models.CharField(blank=True, help_text='환수요일', max_length=10, null=True)),
                ('start', models.DateField(blank=True, help_text='시작일', null=True)),
                ('username', models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(default='created', max_length=250)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type_timelines', to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.BigAutoField(help_text='supplies ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='supplies Name', max_length=40)),
                ('get', models.DateField(blank=True, help_text='구매날짜', null=True)),
                ('price', models.IntegerField(blank=True, default=0, help_text='가격', null=True)),
                ('feed_supplies_id', models.ForeignKey(db_column='feed_supplies_id', on_delete=django.db.models.deletion.PROTECT, related_name='feed_supplies', to='tankManage.feed')),
                ('username', models.ForeignKey(blank=True, default='admin', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Supplies',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(help_text='plants ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='plants Name', max_length=40)),
                ('get', models.DateField(blank=True, help_text='입수날짜', null=True)),
                ('price', models.IntegerField(blank=True, default=0, help_text='가격', null=True)),
                ('feed_plant_id', models.ForeignKey(db_column='feed_plant_id', on_delete=django.db.models.deletion.PROTECT, related_name='feed_plant', to='tankManage.feed')),
                ('username', models.ForeignKey(blank=True, default='admin', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(help_text='fishes ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='fishes Name', max_length=40)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('sex', models.CharField(choices=[('F', '암컷'), ('M', '수컷'), ('N', '설정안함')], default='N', help_text='fishes Sex', max_length=1)),
                ('hmf', models.IntegerField(default=0, help_text='마리수')),
                ('get', models.DateField(blank=True, help_text='입수날짜', null=True)),
                ('price', models.IntegerField(blank=True, default=0, help_text='가격', null=True)),
                ('feed_fish_id', models.ForeignKey(db_column='feed_fish_id', on_delete=django.db.models.deletion.PROTECT, related_name='feed_fish', to='tankManage.feed')),
                ('username', models.ForeignKey(blank=True, default='admin', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Fieshes',
            },
        ),
    ]