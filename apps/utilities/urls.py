from django.conf.urls.defaults import *
urlpatterns = patterns('utilities',
    (r'^sendmail/$', "mail.sendmail"),
    (r'^sendmail_info/thanks/$', "mail.sendmail_2"),
)
