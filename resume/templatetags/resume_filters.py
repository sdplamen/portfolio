from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter(name='replace')
def replace(value, arg):
    try:
        old_char, new_char = arg.split(':')
        return value.replace(old_char, new_char)
    except ValueError:
        return value

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def autoparagrpah(value):
    if not value:
        return ''
    paragraphs = value.split('\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return format_html("".join("<p>{}</p>".format(p) for p in paragraphs))