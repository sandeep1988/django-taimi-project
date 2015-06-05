# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson as json
from django.conf import settings
import requests

def news(request):
    from nouvelles.forms import SubscribeForm
    
    if request.POST:
        subscribeForm = SubscribeForm(request.POST)
        
        if subscribeForm.is_valid():
            try:
                url = "http://idilead.com/webservice/add/contact/"
            
                headers = {
                    "Authorization":"Basic %s" % ( ":".join([settings.ES_API_KEY, settings.ES_API_SECRET]).encode('Base64').replace('\n','') ),
                }
            
                data = {
                    'cont_email':subscribeForm.data['email'],
                    "cont_firstName":subscribeForm.data['firstname'],
                    "cont_name":subscribeForm.data['lastname'],
                    "cont_receive_infoletter":True,
                    "cont_lang":"en",
                    "guid":subscribeForm.data['guid'],
                }
            
                r = requests.post(url, 
                                  headers=headers,
                                  data={'data':"%s" % ( json.dumps(data).encode('Base64').replace('\n','') )})
                
                resp = json.loads(r.text,'utf-8')
                
                if resp['detail'] == "Ok":
                    subscribeForm = SubscribeForm()
                    subscribeForm.msg = {'title':_("Success!"), 'txt':_("Thank you for subscribing!"), 'alert':"success"}
                    
                else:
                    subscribeForm.msg = {'title':_("Error!"), 'txt':_("An error has occured: ") + resp['detail'], 'alert':"error"}
                
            except Exception as e:
                subscribeForm.msg = {'title':_("Error!"), 'txt':_("An error has occured: ") + str(e), 'alert':"error"}
        
    else:
        subscribeForm = SubscribeForm()

    return render_to_response('nouvelles/newspage.html', {'subscribeForm':subscribeForm,
                                                          }, context_instance=RequestContext(request))

def newsletter(request, nid):
    newsletter = None
    error = None
    
    #try:
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

    r = requests.post(url, headers=headers, data={'data':"%s" % ( json.dumps(data).encode('Base64').replace('\n','') )})
        
    resp = json.loads(r.text,'utf-8')
        
    for n in resp['objects']:
        if str(n['id']) == str(nid):
            newsletter = n
            break
        
    #except:
    #    error = _(u"An error has occured with the mailing service, please come back later.") + '<br/>' + str(e)
    
    return render_to_response('nouvelles/newsletter.html', {'newsletter':newsletter,
                                                            'error':error,
                                                            }, context_instance=RequestContext(request))
