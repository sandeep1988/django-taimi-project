from django import template
from nouvelles.models import Nouvelle

register = template.Library()

def nouvelles_list(nbr):
    n = Nouvelle.objects.all().order_by('-date_created')[:nbr]
    return {'news': n}

register.inclusion_tag('recent_news.html')(nouvelles_list)
