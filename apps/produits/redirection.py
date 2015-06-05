# -*- coding: utf-8 -*-
from django.shortcuts import redirect

def swivels(request):
    
    url = request.build_absolute_uri().replace('produits','swivels')
    
    return redirect(url)