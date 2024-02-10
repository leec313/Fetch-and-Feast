from django.shortcuts import render, redirect
from django.db.models import Avg
from django.db.models import Count
from django.contrib import messages
from datetime import datetime, timedelta
from products.models import Product
from blog.models import Post
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

    return render(
        request, 'home/index.html', {'featured_products': featured_products,
                                     'top_liked_posts': top_liked_posts})


def subscribe_newsletter(request):
    """
    Used to post the email the user inputs to the database and
    displays a success/error message
    """
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for subscribing.")
            return redirect('home')
        else:
            messages.error(request, "This email address is already subscribed.")
    else:
        form = NewsletterSubscriptionForm()  # Initialize the form for GET requests

    return render(request, 'home/subscribe_modal.html', {'form': form})
