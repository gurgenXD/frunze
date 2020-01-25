from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def make_phone(value):
    import re
    return re.sub(r'\D', '', value)

register.filter('make_phone', make_phone)