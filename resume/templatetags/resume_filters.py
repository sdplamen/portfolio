from django import template

register = template.Library()

@register.filter
def replace(value, arg):
    """
    Replaces all occurrences of a substring with another string.
    Usage: {{ value|replace:"old_string,new_string" }}
    """
    if isinstance(value, str) and ',' in arg:
        old_string, new_string = arg.split(',', 1)
        return value.replace(old_string, new_string)
    return value

@register.filter
def get_item(dictionary, key):
    """
    Allows dictionary lookup in templates.
    Usage: {{ my_dict|get_item:my_key }}
    """
    return dictionary.get(key)