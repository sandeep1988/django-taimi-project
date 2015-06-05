from django import template
from produits.models import Category, SubCategory

register = template.Library()

def product_cat_list():
    
    cats = Category.objects.all()
    
    return {'cats': cats}

register.inclusion_tag('produits/cats.html')(product_cat_list)

def product_subcat_list(cat_id):
    
    subcats = SubCategory.objects.filter(category__id = cat_id).order_by('order')
    
    return {'subcats': subcats}

register.inclusion_tag('produits/sub_cats.html')(product_subcat_list)