# Generated by Django 3.1.4 on 2021-01-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
    ]