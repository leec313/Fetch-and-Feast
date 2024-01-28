from django.shortcuts import render
from django.db.models import Avg
from products.models import Product


def index(request):
    """Get top-rated products. From the rating model in the product app
    get the average rating and order by highest. Only show first 4"""
    featured_products = Product.objects.annotate(
        avg_rating=Avg('rating__score')).order_by('-avg_rating')[:4]
    return render(
        request, 'home/index.html', {'featured_products': featured_products})
