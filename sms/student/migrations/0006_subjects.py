# Generated by Django 2.2.6 on 2019-11-05 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20191105_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=50)),
                ('classes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassName')),
            ],
        ),
    ]