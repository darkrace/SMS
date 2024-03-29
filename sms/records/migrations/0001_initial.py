# Generated by Django 2.2.6 on 2019-11-05 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0006_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('teacher', models.CharField(max_length=100)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassName')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subjects')),
            ],
        ),
    ]
