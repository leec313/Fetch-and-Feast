from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, ChangePasswordForm

from checkout.models import Order


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    orders = profile.orders.all().order_by('-date')

    # Initialize context
    context = {
        'orders': orders,
        'profile': profile,
        'on_profile_page': True
    }

    if request.method == 'POST':
        # Handle UserProfileForm
        user_profile_form = UserProfileForm(
            request.POST, request.FILES, instance=profile)
        password_form = ChangePasswordForm(user, request.POST)

        # User/Profile info form
        if user_profile_form.is_valid():
            profile = user_profile_form.save(commit=False)
            profile.user.username = user_profile_form.cleaned_data[
                'user_username']
            profile.user.email = user_profile_form.cleaned_data[
                'user_email']
            profile.user.first_name = user_profile_form.cleaned_data[
                'user_first_name']
            profile.user.last_name = user_profile_form.cleaned_data[
                'user_last_name']
            profile.user.save()

            profile.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Please ensure the profile information is valid.')
    else:
        user_profile_form = UserProfileForm(instance=profile)
        password_form = ChangePasswordForm(user)

    context['user_profile_form'] = user_profile_form
    context['password_form'] = password_form

    template = 'profiles/profile.html'
    return render(request, template, context)


@login_required
def change_password(request):
    user = request.user

    if request.method == 'POST':
        # Handle ChangePasswordForm
        password_form = ChangePasswordForm(user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully')
        else:
            messages.error(
                request, 'Password change failed. Please correct the errors.')

    return redirect(reverse('profile'))


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
