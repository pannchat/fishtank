# Generated by Django 3.1.7 on 2021-04-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tankManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='supplies',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
