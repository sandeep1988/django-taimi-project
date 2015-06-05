from cms.app_base import CMSApp
from django.utils.translation import ugettext_lazy as _
from cms.apphook_pool import apphook_pool

class CalculatorMyApphook(CMSApp):
    name = _("Calculator")
    urls = ["taimi_calculator.urls"]

apphook_pool.register(CalculatorMyApphook)
