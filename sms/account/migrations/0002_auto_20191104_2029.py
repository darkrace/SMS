# Generated by Django 2.2.6 on 2019-11-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'SubAdmin'), (3, 'Staff'), (4, 'Management'), (5, 'Student')], default=1),
        ),
    ]
