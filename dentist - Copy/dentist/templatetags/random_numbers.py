import random
import datetime
from django import template

register = template.Library()

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.simple_tag
def current_date():
    return datetime.date.today()