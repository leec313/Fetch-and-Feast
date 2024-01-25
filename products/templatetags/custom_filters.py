from django import template

register = template.Library()


@register.filter(name='range_value')
def range_value(value):
    return range(value)
