# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.conf import settings
from django import template
import requests

register = template.Library()

def eazisale_newsletters():
    error = None

    try:
        url = "http://idilead.com/webservice/list/email/"

        headers = {
            "Authorization":"Basic %s" % ( ":".join([settings.ES_API_KEY, settings.ES_API_SECRET]).encode('Base64').replace('\n','') ),
        }

        data = {
            'filter_default_cat':"ABIL",
            'sent':1,
            'sort':"created",
            'asc':0,
        }

        r = requests.post(url, 
                          headers=headers,
                          data={'data':"%s" % ( json.dumps(data).encode('Base64').replace('\n','') )})
        
        resp = json.loads(r.text,'utf-8')
        newsletters = resp['objects']
        
        for i, newsletter in enumerate(newsletters):
            newsletters[i]['url'] = reverse('nouvelles.views.newsletter', args=[newsletter['id']])
        
    except Exception as e:
        newsletters = []
        error = _(u"An error has occured with the mailing service, please come back later.") + '<br/>' + str(e)
    
    return {'newsletters':newsletters, 'error':error,}

register.inclusion_tag('nouvelles/eazisale_newsletters.html')(eazisale_newsletters)

def footerSubscribeForm(nbr = None):
    from nouvelles.forms import SubscribeForm
    subscribeForm = SubscribeForm()
    return {'subscribeForm': subscribeForm}

register.inclusion_tag('nouvelles/footerSubscribeForm.html')(footerSubscribeForm)