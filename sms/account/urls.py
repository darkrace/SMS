from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

