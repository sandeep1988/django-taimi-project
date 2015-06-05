from produits.menu import SubCategoryMenu
from cms.app_base import CMSApp
from django.utils.translation import ugettext_lazy as _
from cms.apphook_pool import apphook_pool

class MyApphook(CMSApp):
    name = _("Produits")
    urls = ["produits.urls"]

apphook_pool.register(MyApphook)
