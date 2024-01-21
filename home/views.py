from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile


@login_required
def index(request):
    """ A view to return the index page and allow access
    to the user profile model to view the profile image """

    user = request.user
    profile = UserProfile.objects.get(user=user)

    context = {
        'profile': profile,
    }

    return render(request, 'home/index.html', context)
