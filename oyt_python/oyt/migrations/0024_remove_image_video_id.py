# Generated by Django 3.2 on 2022-07-26 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0023_video_img_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='video_id',
        ),
    ]
