# myapp/templatetags/extra_tags.py

from django import template

register = template.Library()

@register.simple_tag
def get_range(start, end):
    return range(int(start), int(end))
