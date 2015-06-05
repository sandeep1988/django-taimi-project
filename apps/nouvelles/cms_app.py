from produits.menu import SubCategoryMenu
from cms.app_base import CMSApp
from django.utils.translation import ugettext_lazy as _
from cms.apphook_pool import apphook_pool

class NewsApp(CMSApp):
    name = _("Nouvelles")
    urls = ["nouvelles.urls"]

apphook_pool.register(NewsApp)
