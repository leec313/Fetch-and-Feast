from django.shortcuts import render, redirect
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
        send_mail(
            subject='Fetch & Feast: Thanks fo Subscribing!',
            message='Get ready for some PAWSOME newseletters coming your way!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
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
