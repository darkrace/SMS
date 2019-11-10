# Generated by Django 2.2.6 on 2019-11-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'SubAdmin'), (3, 'Staff'), (4, 'Management'), (5, 'Student')], default=5)),
                ('fullname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('user', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('email_verify', models.BooleanField(default=False)),
                ('phone_verify', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
