from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.simple import direct_to_template
#from filebrowser.sites import site

admin.autodiscover()

urlpatterns = i18n_patterns('',
	#url(r'^admin/filebrowser/', include(site.urls)),
	(r'^tinymce/', include('tinymce.urls')),
	(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^produits/', "produits.redirection.swivels"),
	url(r'^utilities/', include("utilities.urls")),
	url(r'^robots.txt', direct_to_template, {"template":"robots.txt"}),
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
