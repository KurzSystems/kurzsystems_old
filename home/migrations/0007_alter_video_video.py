# Generated by Django 3.2.4 on 2021-06-23 11:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='video'),
        ),
    ]
