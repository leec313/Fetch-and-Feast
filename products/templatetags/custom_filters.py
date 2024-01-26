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
