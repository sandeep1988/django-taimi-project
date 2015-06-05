from django.contrib.syndication.views import Feed
from nouvelles.models import Nouvelle
from django.conf import settings

class NouvellesFeed(Feed):
    title = "Nouvelles de " + settings.NOM_CLIENT
    link = "/nouvelles/"
    description = "Nouvelles du website de " + settings.NOM_CLIENT

    def items(self):
        return Nouvelle.objects.all().order_by('-date_created')[:5]

    def item_title(self, item):
        return item.titre

    def item_link(self, item):
	mystr = 'http://127.0.0.1/nouvelles/' + item.slug
        return mystr

    def item_description(self, item):
        return item.description
