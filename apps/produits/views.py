# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.http import HttpResponse
import datetime
import json
from django.core import serializers
import locale
import time, operator
from produits.models import *
from django.db.models import Q
import string
import client
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

def search(request):
    terms = request.GET['search'].split("%20")
    products = list(Product.objects.filter(reduce(operator.and_, (Q(part_no__icontains=x) for x in terms))))
    products1 = list(Product.objects.filter(reduce(operator.and_, (Q(seal_kit__icontains=x) for x in terms))))
    if len(products1) > 0:
        products.extend(products1)
    products1 = list(Product.objects.filter(reduce(operator.and_, (Q(subcategory__title__icontains=x) for x in terms))))
    if len(products1) > 0:
        products.extend(products1)
    return render_to_response('recherche.html', {'products': products}, context_instance=RequestContext(request))

def getSubCats(request, cat):
    exclude = set(string.punctuation)
    cat = Category.objects.get(slug = cat)
    subcats = SubCategory.objects.filter(category = cat)
    
    request.current_page = {}
    request.current_page['get_menu_title'] = cat
    request.current_page['get_meta_description'] = cat.description
    request.current_page['get_meta_keywords'] = ''
    request.current_page['get_page_title'] = cat
    return render_to_response('produits/list_produits_cat.html', {'subcats': subcats, 'cat' : cat, 'products' : True}, context_instance=RequestContext(request))

def getProducts(request, cat, subcat):
    
    exclude = set(string.punctuation)
    request.current_page = {}
    products = Product.objects.filter(subcategory__slug = subcat)
    request.current_page['get_menu_title'] = products[0].subcategory.title
    request.current_page['get_page_title'] = products[0].subcategory.title

    request.current_page = {}
    request.current_page['get_menu_title'] = products[0].subcategory.category.title + ' | ' + products[0].subcategory.title
    request.current_page['get_meta_description'] = products[0].subcategory.category.description.encode('utf-8', 'replace')
    request.current_page['get_meta_keywords'] = ''
    
    page_title = '<a style="font-size: 24px;" href="/swivels/' + products[0].subcategory.category.slug + '/">' + products[0].subcategory.category.title + '</a><br/><span style="font-size: 14px">' + products[0].subcategory.title + '</span>'
    
    return render_to_response('produits/produit_detail.html', {'products': products, 'page_title': page_title}, context_instance=RequestContext(request))

def addProductInfo(request, pid):
    if not "products" in request.session:
        request.session['products'] = []
    product = Product.objects.get(id = pid)
    if not product in request.session['products']:
        request.session['products'].append(product)
    else:
        return HttpResponse(_('Product already in your information request'))
    print request.session['products']
    request.session.modified = True
    return HttpResponse(_('Product successfully added to your information request, click <a href="/en/swivels/listinfo/">here</a> to see your request.'))

def removeProductInfo(request, pid):
    product = Product.objects.get(id = pid)
    if product in request.session['products']:
        request.session['products'].remove(product)
    print request.session['products']
    request.session.modified = True
    return HttpResponse(_('Product successfully removed from your information request'))

def listProductInfo(request):
    if not "products" in request.session:
        request.session['products'] = []
    products = request.session['products']
    return render_to_response('info_request.html', {'products': products}, context_instance=RequestContext(request))

def getIndex(request):

    return render_to_response('produits/list_produits.html', {}, context_instance=RequestContext(request))
    