# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.utils import simplejson as json
from django.conf import settings

def sendmail(request):
    message = render_to_string(
        'utilities/contactmail.html',
        {
            'nom': request.POST['name'], 'courriel': request.POST['email'], 'message': request.POST['message'],
            'country':request.POST['country'],'postal_code':request.POST['postal_code']
        })
    msg = EmailMultiAlternatives('TAIMI - Message from '+request.POST['email'], '', request.POST['email'], ["info@taimi.ca"])
    msg.attach_alternative(message, "text/html")
    msg.send()
    return render_to_response('contact.html', {'message':"Your message has been sent".decode('utf-8')}, context_instance=RequestContext(request))

def sendmail_2(request):
    if not "products" in request.session:
        request.session['products'] = []
        
    message = render_to_string(
        'utilities/info_mail.html',
        {
            'nom': request.POST['name'],
            'courriel': request.POST['email'], 
            'message': request.POST['message'], 
            "products" : request.session['products'],
            "country":request.POST['country'],
            "postal_code":request.POST['postal_code'],
        })
    
    msg = EmailMultiAlternatives('TAIMI - Info request from '+request.POST['email'], '', request.POST['email'], ["info@taimi.ca"]) #info@taimi.ca
    msg.attach_alternative(message, "text/html")
    msg.send()
    
    tmp = request.POST['name'].split(' ')
    firstname = tmp[0]
    if len(tmp) > 1:
        lastname = tmp[1]
    else:
        lastname = ""
    
    url = "http://idilead.com/webservice/add/contact/"

    headers = {
        "Authorization":"Basic %s" % ( ":".join([settings.ES_API_KEY, settings.ES_API_SECRET]).encode('Base64').replace('\n','') ),
    }

    data = {
        'cont_email':request.POST['email'],
        "cont_country":request.POST['country'],
        "cont_postalCode":request.POST['postal_code'],
        "guid":request.POST['guid'],
        "cont_firstName":firstname,
        "cont_name":lastname,
    }

    r = requests.post(url, 
                      headers=headers,
                      data={'data':"%s" % ( json.dumps(data).encode('Base64').replace('\n','') )})
    
    resp = json.loads(r.text,'utf-8')
    
    request.session['products'] = []
    request.session.modified = True
    
    return render_to_response('info_request.html', {'message':"Your message has been sent".decode('utf-8')}, context_instance=RequestContext(request))
