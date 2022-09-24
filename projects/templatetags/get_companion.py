from django import template
from accounts.models import *
register = template.Library()
@register.simple_tag
def get_companion(user, ch):
   for u in ch.members.all():
       if u != user:
           return u
   return None  
