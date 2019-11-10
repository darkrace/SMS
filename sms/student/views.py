from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Student, ClassName
from records.models import TimeTable
from django.http import HttpResponse
# Create your views here.


# class StudentView(View):
#     template_name = 'student/student.html'
#
#     def get(self, request, *args, **kwargs):
#         obj = Student.objects.all()
#         context = {'obj': obj}
#
#         return render(request, self.template_name, context)
#
#
# class Classes(View):
#     template_name = 'student/classes.html'
#
#     def get(self, request, *args, **kwargs):
#         object = ClassName.objects.all()
#         context = {'object': object}
#
#         return render(request, self.template_name, context)

class Student_Dashboard(View):
    templates_name = 'student/pages/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


class TimeTableView(View):
    templates_name = 'student/pages/time_table.html'

    def get(self, request, *args, **kwargs):
        object = TimeTable.objects.all()
        context = {'time_table_obj': object}
        return render(request, self.templates_name, context)


class ResultView(View):
    templates_name = 'student/pages/result.html'

    def get(self, request, *args, **kwargs):
        obj = Student.objects.all()
        return render(request, self.templates_name, {'obj': obj})


class CourseOutLinetView(View):
    templates_name = 'student/pages/course_outline.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


class HomeView(View):
    templates_name = 'student/pages/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


class CourseView(View):
    templates_name = 'student/pages/course.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


def index(request):
    obj = ClassName.objects.all()
    return render(request, 'student/slug.html', {'obj': obj})


class Slug_Detail(View):
    template_name = 'student/slug_detail.html'

    def get(self, request, slug, *args, **kwargs ):
        slug = get_object_or_404(ClassName, slug=slug)

        std = self.student()

        context = {'slug': slug, 'std': std}

        return render(request, self.template_name, context)

    def student(self):
        student = Student.objects.all()
        return student





