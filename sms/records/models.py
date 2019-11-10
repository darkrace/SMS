from django.db import models
from student.models import ClassName, Subjects
# Create your models here.


class TimeTable(models.Model):
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.classname
