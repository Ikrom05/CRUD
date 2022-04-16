from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/users/sign_in')

# Create your views here.
from users.forms import SignUpForm, SignInForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(requet):
    if requet.method == 'POST':
        form = SignInForm(data=requet.POST)
        if form.is_valid():
            user = form.get_user()
            login(requet, user)
            if 'next' in requet.POST:
                return redirect(requet.POST.get('next'))
            return redirect('article_func')
    form = SignInForm()
    return render(requet, 'sign_in.html', {'form':form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')