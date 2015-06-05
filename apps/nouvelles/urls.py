from django.conf.urls.defaults import *

urlpatterns = patterns('nouvelles.views',
    url(r'^$', 'news', name="news_page"),
    url(r'^(?P<nid>.+)/$', 'newsletter', name="newsletter"),
)
