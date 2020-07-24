from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail, EmailMultiAlternatives
# from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import LoginForm, SignUpForm

USER = get_user_model()

# @login_required
def home(request):
    # html_file = get_template('mail_template.html')
    # html_content = html_file.render()
    # subject = 'Test'
    # from_email = 'admin@admin.com'
    # to = ['subhamaharjan13@gmail.com']
    # msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to)
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()
    return render(request, 'webapp/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                print("a user is found", user)
                login(request, user)
                return redirect('/webapp/profile/')
            else:
                print("auth credentials do not match")
            print(form.cleaned_data)
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/webapp/profile/')
        form = LoginForm()
    return render(request, 
                  'webapp/login.html', 
                  {'form': form})

@login_required
def profile_view(request):
    return render(request, 'webapp/profile.html')


def logout_view(request):
    logout(request)
    return redirect('/webapp/login/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            user = USER(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/webapp/login/')
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'webapp/signup.html', {'form': form})
