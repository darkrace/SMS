from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from sms.utils import unique_slug_generator
from account.models import User
# Create your models here.


class ClassName(models.Model):
    class_name = models.CharField(max_length=30)
    section_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse("single_slug", args=[self.slug])


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.class_name, instance.slug)


pre_save.connect(slug_save, sender=ClassName)


class Student(models.Model):

    class_id = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    type = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    age = models.DateField()
    address = models.TextField()
    guardient = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_detail", args=[self.pk])


class Fee(models.Model):
    CHOICES = (
        ('yellow', 'YELLOW'),
        ('green', 'GREEN'),
        ('red', 'RED'),
    )

    student_id = models.ForeignKey(Student, on_delete=models.CharField)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=CHOICES, default='yellow')

    def __str__(self):
        return self.student_id.name


class Subjects(models.Model):
    subjects = models.CharField(max_length=50)
    classes_id = models.ForeignKey(ClassName, on_delete=models.CASCADE)

    def __str__(self):
        return self.subjects