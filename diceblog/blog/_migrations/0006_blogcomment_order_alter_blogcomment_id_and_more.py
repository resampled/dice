# Generated by Django 5.1 on 2024-08-26 08:43

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_id_alter_blogpost_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='order',
            field=models.FloatField(default=blog.models.make_order),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='id',
            field=models.SlugField(default='75thiqtn', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.SlugField(default='0scium51', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='order',
            field=models.FloatField(default=blog.models.make_order),
        ),
    ]
