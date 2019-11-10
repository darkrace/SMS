from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegisterForm
from django.views.generic import View
from django.contrib.auth.models import auth
from django.contrib import messages
from student.models import Student
from .models import User


class IndexView(View):
    templates_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                if user.user_type == 1:
                    # print(request.POST['email'])
                    messages.info(request, 'Welcome to SubAdmin Dashboard')
                    return redirect('account:login')
                    # return HttpResponseRedirect(reverse('profiles:pro_admin_index'))
                elif user.user_type == 2:
                    # print(request.POST['email'])
                    messages.info(request, 'Welcome to Staff Dashboard')
                    return redirect('account:login')
                    # return HttpResponseRedirect(reverse('profiles:pro_index'))
                elif user.user_type == 3:
                    # print(request.POST['email'])
                    messages.info(request, 'Welcome to Staff Dashboard')
                    return redirect('account:login')
                    # return HttpResponseRedirect(reverse('account:profile'))
                elif user.user_type == 4:
                    # print(request.POST['email'])
                    messages.info(request, 'Welcome to Management Dashboard')
                    return redirect('account:login')
                    # return HttpResponseRedirect(reverse('account:profile'))
                elif user.user_type == 5:
                    # print(request.POST['email'])
                    # messages.info(request, 'Welcome to Student Dashboard')
                    # return redirect('account:login')
                    print(user.id)
                    return HttpResponseRedirect(reverse('student:index_view'))
                else:
                    messages.info(request, 'The User You Enter are not found')
                    return redirect('account:login')
                    # return HttpResponseRedirect(reverse('accounts:staff_profile'))
            else:
                messages.info(request, 'invalid credential')
                return redirect('account:login')
        else:
            return render(request, self.template_name,)


class UserRegisterView(View):
    template_name = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        #GetMethod
        form = RegisterForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #PostMethod
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        # return HttpResponse('LogOut')
        return HttpResponseRedirect(reverse('account:index'))