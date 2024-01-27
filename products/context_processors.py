# context_processors.py

from .models import Product


def average_rating(request):
    products = Product.objects.all()
    rating_dict = {}

    for product in products:
        average_rating = product.average_rating()
        rating_dict[product.id] = average_rating

    return {'average_ratings': rating_dict, 'request': request}
