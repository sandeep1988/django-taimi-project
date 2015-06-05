#from django.db import models
#from django.utils.translation import ugettext_lazy as _
from cms.models.pagemodel import Page
#from cms.models import Title
from menus.base import NavigationNode
#from produits.models import Category
 
#class PageDesc(models.Model):
#	page = models.ForeignKey(Page, unique=True, related_name="extended_fields")
#	description = models.CharField(max_length=200)
#def _description(obj):
#	for e_f in obj.extended_fields.all():
#		return e_f.description
#	return None


#Page._description = _description
#Page.description = property(lambda u: u._description)
#from menus.base import NavigationNode
NavigationNode.page_instance = lambda u: Page.objects.filter(pk = u.id)[0] 


def _app_pages(self):
	nn = self.children
	nn = [n for n in nn if not n.id % 154332345]
	return nn

NavigationNode.app_pages = _app_pages


		
	
	
