# Generated by Django 5.1 on 2024-09-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_bloguser_username_blogpost_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='id',
            field=models.SlugField(default='wvhyig4dbu3nq918m2', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.SlugField(default='x0xcg032', primary_key=True, serialize=False, unique=True),
        ),
    ]
