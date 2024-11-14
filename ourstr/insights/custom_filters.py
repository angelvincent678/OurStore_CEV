from django import template

register = template.Library()

# Custom filter to access a dictionary by key
@register.filter
def get_item(dictionary, key):
    """Returns the value for a given key in a dictionary."""
    return dictionary.get(key)
