# Generated by Django 2.2.6 on 2019-11-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20191104_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classname',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
