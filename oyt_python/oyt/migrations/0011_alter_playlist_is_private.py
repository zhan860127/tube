# Generated by Django 3.2 on 2021-04-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0010_auto_20210411_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
