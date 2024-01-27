# context_processors.py

from .models import Product


def average_rating(request):
    """ Allows us to access the average rating
    throughout all areas of the project """
    products = Product.objects.all()
    rating_dict = {}

    for product in products:
        average_rating = product.average_rating()
        rating_dict[product.id] = average_rating

    return {'average_ratings': rating_dict, 'request': request}
