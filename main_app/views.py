from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    """Home page."""
    return render(request, 'main_app/index.html')

@login_required
def new_profile(request):
    """Page allowing the user to fill all the informations about his couple."""
    if request.method != 'POST':
        form = UserProfileForm()
    else:
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.owner = request.user
            new_profile.save()
            return redirect('main_app:profile')

    context = {'form': form}
    return render(request, 'main_app/new_profile.html', context)
