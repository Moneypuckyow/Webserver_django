# Generated by Django 3.1.2 on 2020-11-01 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]