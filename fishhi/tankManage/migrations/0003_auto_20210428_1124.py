# Generated by Django 3.1.7 on 2021-04-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tankManage', '0002_auto_20210428_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='depth',
            field=models.IntegerField(blank=True, help_text='depth', null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='height',
            field=models.IntegerField(blank=True, help_text='height', null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='width',
            field=models.IntegerField(blank=True, help_text='width', null=True),
        ),
    ]
