from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView

class SignUpView(View):
    """Signup view."""
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    """Login view."""
    form_class = LoginForm
    template_name = 'login.html'
