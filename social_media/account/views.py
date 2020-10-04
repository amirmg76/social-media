from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm


@login_required
def dashboard(request):
    context = {'section': 'dashboard'}
    return render(request, 'account/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            context = {'new_user': new_user}
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {'user_form': user_form}
        return render(request, 'account/register.html', context)
