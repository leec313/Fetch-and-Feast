import uuid
from django.shortcuts import render, redirect, reverse
from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from datetime import datetime, timedelta
from products.models import Product
from blog.models import Post
from profiles.models import UserProfile, NewsletterSubscription
from .forms import NewsletterSubscriptionForm


def index(request):
    """Get top-rated products and top-liked posts."""
    # Get top-rated products
    featured_products = Product.objects.annotate(
        avg_rating=Avg('rating__score')).order_by('-avg_rating')[:4]

    # Get top-liked posts within the last month
    last_month = datetime.now() - timedelta(days=30)
    top_liked_posts = Post.objects.filter(created_on__gte=last_month).annotate(
        num_likes=Count('likes')).order_by('-num_likes')[:4]

    # Initialize the NewsletterSubscriptionForm
    form = NewsletterSubscriptionForm()

    context = {
        'featured_products': featured_products,
        'top_liked_posts': top_liked_posts,
        'form': form
    }

    return render(
        request, 'home/index.html', context)


# Allows us to get the user and associate newsletter
User = get_user_model()


def subscribe_newsletter(request):
    """
    View for newsletter subscription modal/index page
    """
    if request.method == 'POST':
        email = request.POST.get('email')

        # Send email to admin
        send_mail(
            subject=f'New Newsletter Subscription: {email}',
            message=f'{email} has subscribed to the newsletter!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        # Send email to user
        # creates unsubscribe url (works for anonymous users)
        unsubscribe_url = request.build_absolute_uri(
            reverse('unsubscribe_newsletter') + f'?email={email}')
        unsubscribe_message = (
            f'To unsubscribe from our newsletter, click '
            f'<a href="{unsubscribe_url}">here</a>.'
        )
        send_mail(
            subject='Fetch & Feast: Thanks for Subscribing!',
            message=(
                f'Get ready for some PAWSOME newsletters coming your way! '
                f'{unsubscribe_message}'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=(
                f'<p>Get ready for some PAWSOME newsletters coming your way!'
                f'{unsubscribe_message}</p>'
            )
        )

        # Check if the email is already subscribed
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.info(
                request, 'You are already subscribed to the newsletter.')
            return redirect('home')  # Redirect to the home page

        # If user is authenticated associate the subscription w/ their profile
        if request.user.is_authenticated:
            user_profile = request.user.userprofile
            user_profile.subscribe_newsletter = True
            user_profile.save()
        else:
            # Check if a user with this email already exists
            user = User.objects.filter(email=email).first()
            if user:
                # If the user exists, use their existing UserProfile
                user_profile = user.userprofile
                user_profile.subscribe_newsletter = True
                user_profile.save()
            else:
                # If the user does not exist, create a UserProfile
                user_profile = UserProfile.objects.create(
                    default_email=email, subscribe_newsletter=True)

        # Create NewsletterSubscription object
        NewsletterSubscription.objects.create(
            user_profile=user_profile, email=email)

        messages.success(request, 'Subscription successful!')
        return redirect('home')  # Redirect to the home page


def unsubscribe_newsletter(request):
    # Retrieve email from the request or query parameters
    email = request.GET.get('email')

    if email:
        # Check if the email is provided
        subscription_entry = NewsletterSubscription.objects.filter(email=email).first()

        if subscription_entry:
            # If the user's email is found, delete the entry
            subscription_entry.delete()

        # Mark the user as unsubscribed in the UserProfile
        if request.user.is_authenticated:
            request.user.userprofile.subscribe_newsletter = False
            request.user.userprofile.save()
        else:
            # If user is not logged in, find the UserProfile by email and update it
            user = User.objects.filter(email=email).first()
            if user:
                user_profile = UserProfile.objects.get_or_create(user=user)[0]
                user_profile.subscribe_newsletter = False
                user_profile.save()

        # Display a success message
        messages.success(request, 'You have successfully unsubscribed from the newsletter.')
    else:
        # Display an error message if email is not provided
        messages.error(request, 'Email address is required to unsubscribe.')

    # Redirect to the home page
    return redirect('home')