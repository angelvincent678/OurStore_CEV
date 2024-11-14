from django import template

register = template.Library()

# Define a custom multiply filter
@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0  # Return 0 if there is an error
