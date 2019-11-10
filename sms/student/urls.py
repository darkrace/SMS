from django.urls import  path
from .views import *

app_name = 'student'

urlpatterns = [
    # path('std/', StudentView.as_view(), name='student_index'),
    # path('class/', Classes.as_view(), name='class_name'),
    path('dashboard/', Student_Dashboard.as_view(), name='index_view'),
    path('slug/', index, name='index'),
    path('slug/<slug>/', Slug_Detail.as_view(), name='single_slug'),
    path('timetable/', TimeTableView.as_view(), name='time_table'),
    path('result/', ResultView.as_view(), name='result'),
    path('courseoutline/', CourseOutLinetView.as_view(), name='courseoutline'),
    path('home/', HomeView.as_view(), name='home'),
    path('course/', CourseView.as_view(), name='course'),

]