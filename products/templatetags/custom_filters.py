from django import template

register = template.Library()


@register.filter(name='range_value')
def range_value(value):
    """
    Given a numeric value, return a range object from 0 to that value.
    """
    return range(value)


@register.filter
def get_profile_image_url(user_id, rating_profiles):
    """
    Given a user ID and a dictionary of rating profiles,
    return the profile image URL for the user.
    If the user ID is not found in the dictionary, return an empty string.
    """
    return rating_profiles.get(user_id, '')


@register.filter(name='stars')
def stars(value):
    """Round the average rating to the nearest whole number
    and display as star icons from Font Awesome"""
    rounded_value = round(value)

    # Create a string with Font Awesome icons
    stars_string = ''.join([
        '<i class="fas fa-star fas-star-solid"></i>' for _ in range(
            rounded_value)
    ])

    stars_string += ''.join([
        '<i class="far fa-star far-star-outline"></i>' for _ in range(
            5 - rounded_value)
    ])

    return stars_string