from django.contrib.auth.views import FormView
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect #, render
# from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm, SignUpForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'webapp/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            print("a user is found", user)
            login(self.request, user)
            return redirect('/webapp/profile/')
        else:
            print("auth credentials do not match")
            print(form.cleaned_data)
            return self.form_invalid(form)


class ProfileView(TemplateView):
    template_name = "webapp/profile.html"


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('/webapp/log-in/')


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'webapp/signup.html'
    USER = get_user_model()

    def form_valid(self, form):
        user = self.USER(username=form.cleaned_data['username'],
                         first_name=form.cleaned_data['first_name'],
                         last_name=form.cleaned_data['last_name'],
                         email=form.cleaned_data['email'])
        user.set_password(form.cleaned_data['password'])
        user.save()

        return redirect('/webapp/log-in/')
