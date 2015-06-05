from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('taimi_calculator.views',
    url(r'', 'index', name="calculator"),
)
