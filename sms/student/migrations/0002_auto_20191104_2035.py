# Generated by Django 2.2.6 on 2019-11-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classname',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
