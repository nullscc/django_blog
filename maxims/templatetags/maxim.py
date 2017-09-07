from django.template import Library
from ..models import Maxim
import random
register = Library()



@register.simple_tag
def get_maxim():
    count = Maxim.objects.count()
    rint = random.randint(1, count-1)
    res = Maxim.objects.skip(rint).limit(1).first()
    
    return res