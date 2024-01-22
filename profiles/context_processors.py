from .models import UserProfile


def profile_image(request):
    """ This will allow us to display the 
    profile image (if it exists) on all templates """
    profile_image = None
    if request.user.is_authenticated:
        try:
            profile_image = request.user.userprofile.profile_image.url
        except UserProfile.DoesNotExist:
            pass

    return {'profile_image': profile_image}
