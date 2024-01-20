from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UserInformationForm, UserProfileImageForm

from checkout.models import Order


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        user_form = UserInformationForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        image_form = UserProfileImageForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid() and image_form.is_valid():
            user_form.save()
            profile_form.save()
            image_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        user_form = UserInformationForm(instance=user)
        profile_form = UserProfileForm(instance=profile)
        image_form = UserProfileImageForm(instance=profile)

    orders = profile.orders.all().order_by('-date')
    template = 'profiles/profile.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'image_form': image_form,
        'orders': orders,
        'profile': profile,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)