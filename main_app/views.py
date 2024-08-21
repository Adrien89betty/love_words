from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import NewProfileForm

def index(request):
    """Home page."""
    return render(request, 'main_app/index.html')

@login_required
def new_profile(request):
    """Page allowing the user to fill all the information about his couple."""
    if request.method == 'POST':
        form = NewProfileForm(data=request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('main_app:show_profile')
    else:
        form = NewProfileForm()

    context = {'form': form}
    return render(request, 'main_app/new_profile.html', context)


@login_required
def show_profile(request):
    """Show the user profile."""
    profile = UserProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'main_app/user_profile.html', context)
