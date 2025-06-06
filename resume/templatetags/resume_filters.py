from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter(name='replace')
def replace(value, arg):
    """
    Replaces all occurrences of string arg[0] with arg[1] in value.
    Usage: {{ value|replace:"old_string":"new_string" }}
    """
    try:
        old_char, new_char = arg.split(':')
        return value.replace(old_char, new_char)
    except ValueError:
        return value # Return original value if arg format is incorrect

@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Allows dictionary key lookup in templates.
    Usage: {{ dictionary|get_item:key }}
    """
    return dictionary.get(key)

@register.filter
def autoparagrpah(value):
    """
    Converts newline characters in a string into HTML paragraphs.
    """
    if not value:
        return ''
    paragraphs = value.split('\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return format_html("".join("<p>{}</p>".format(p) for p in paragraphs))