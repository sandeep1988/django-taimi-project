# -*- coding: utf-8 -*-.
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

def index(request):
    
    multiplication_time = 0
    oil_price = 0
    
    one_inch_swivel_cost = 0
    one_inch_swivel_taimi_cost = 0
    one_inch_swivel_number = 0
    
    three_quart_swivel_cost = 0
    three_quart_swivel_taimi_cost = 0
    three_quart_swivel_number = 0
    
    dollar_sign = '$'

    hose_number = 0
    downtime_number = 0
    cost_hose_replacement = 0
    
    if request.POST:
        
        equipment = request.POST['equipment']
        location = request.POST['location']
        swivels_type = request.POST['swivels_type']
        hours_worked = request.POST['hours_worked']
        
        #Set var for equipment
        if equipment == 'harvester':
            
            one_inch_swivel_number = 2
            three_quart_swivel_number= 2
            hose_number = 4
        
        elif equipment == 'rotation':
            
            one_inch_swivel_number = 2
            three_quart_swivel_number= 5
            hose_number = 7
            
        #Set var for location
        
        if location == 'america':
            
            oil_price = 15
            one_inch_swivel_taimi_cost = 199
            three_quart_swivel_taimi_cost = 169
            dollar_sign = '$'
            
        elif location == 'europe':
            
            oil_price = 30
            one_inch_swivel_taimi_cost = 165
            three_quart_swivel_taimi_cost = 125
            dollar_sign = '€'
            
        #Set var for type of swivels
        
        if swivels_type == 'none' and location == 'america':
            
            one_inch_swivel_cost = 0
            three_quart_swivel_cost = 0
            downtime_number = 15
            multiplication_time = 5
            cost_hose_replacement = 12000
            
        if swivels_type == 'none' and location == 'europe':
            
            one_inch_swivel_cost = 0
            three_quart_swivel_cost = 0
            downtime_number = 15
            multiplication_time = 5

        #Swivels type Ball Bearing Swivels
            
        elif swivels_type == 'ball' and location == 'america':
            
            one_inch_swivel_cost = 50
            three_quart_swivel_cost = 40
            downtime_number = 10
            multiplication_time = 10
            
        elif swivels_type == 'ball' and location == 'europe':
            
            one_inch_swivel_cost = 60
            three_quart_swivel_cost = 50
            downtime_number = 10
            multiplication_time = 10
        
        #Swivels type Heavy Duty Ball Bearing Swivels
         
        elif swivels_type == 'heavy' and location == 'america':
            
            one_inch_swivel_cost = 86
            three_quart_swivel_cost = 63
            downtime_number = 6
            multiplication_time = 6
            
        #Il n'y a pas de cette sorte en Europe
 
        elif swivels_type == 'needle' and location == 'europe':
            
            one_inch_swivel_cost = 159
            three_quart_swivel_cost = 109
            downtime_number = 3
            multiplication_time = 3
            
        #Il n'y a pas de cette sorte en Amérique

        elif swivels_type == 'dontknow' and location == 'america':
            
            one_inch_swivel_cost = 68
            three_quart_swivel_cost = 52
            downtime_number = 8
            multiplication_time = 8
            
        elif swivels_type == 'dontknow' and location == 'europe':
            
            one_inch_swivel_cost = 100
            three_quart_swivel_cost = 75
            downtime_number = 5
            multiplication_time = 5
        
        #set cost of hose replacement
        if equipment == 'harvester' and swivels_type == 'none':
            cost_hose_replacement = 12000
        
        elif equipment == 'rotation' and swivels_type == 'none':
            cost_hose_replacement = 18000
        
        #calcul ----------------------------------
        
        #print 'downtimenumber: ' + str(downtime_number)
        #print 'one_inch_swivel_number: ' + str(one_inch_swivel_number)
        #print 'three_quart_swivel_number: ' + str(three_quart_swivel_number)
        #var for the competitor
        total_one_inch_swivel_cost = one_inch_swivel_cost * one_inch_swivel_number * downtime_number
        #print 'total_one_inch_swivel_cost: ' + str(total_one_inch_swivel_cost)
        
        total_three_quart_swivel_cost = three_quart_swivel_cost  * three_quart_swivel_number * downtime_number
        #print 'total_three_quart_swivel_cost: ' + str(total_three_quart_swivel_cost)
        
        cost_downtime_caused_swivel = downtime_number * 0.25 * 200 * (one_inch_swivel_number + three_quart_swivel_number)
        #print 'cost_downtime_caused_swivel: ' + str(cost_downtime_caused_swivel)
        
        
        cost_oil_leak_caused_swivel = oil_price * (one_inch_swivel_number + three_quart_swivel_number) * 0.25 * downtime_number
        #print 'cost_oil_leak_caused_swivel: ' + str(cost_oil_leak_caused_swivel)
        
        #cost of hose replacement
        #print 'cost_hose_replacement: ' + str(cost_hose_replacement)
        
        #total cost for the competitor
        total_cost_competitor = total_one_inch_swivel_cost + total_three_quart_swivel_cost + cost_downtime_caused_swivel + cost_oil_leak_caused_swivel + cost_hose_replacement
        #print 'total_cost_competitor: ' + str(total_cost_competitor)
        
        #print '------VAR FOR TAIMI-------'
        
        #var for taimi
        total_one_inch_swivel_taimi_cost = one_inch_swivel_taimi_cost * one_inch_swivel_number
        #print 'total_one_inch_swivel_taimi_cost: ' + str(total_one_inch_swivel_taimi_cost)
        
        total_three_quart_swivel_taimi_cost = three_quart_swivel_taimi_cost * three_quart_swivel_number
        #print 'total_three_quart_swivel_taimi_cost: ' + str(total_three_quart_swivel_taimi_cost)
        
        cost_downtime_caused_swivel_taimi =  cost_downtime_caused_swivel / multiplication_time
        #print 'cost_downtime_caused_swivel_taimi: ' + str(cost_downtime_caused_swivel_taimi)
        
        cost_oil_leak_caused_swivel_taimi = cost_oil_leak_caused_swivel / multiplication_time
        #print 'cost_oil_leak_caused_swivel_taimi: ' + str(cost_oil_leak_caused_swivel_taimi)
        
        cost_hose_replacement_taimi = cost_hose_replacement / multiplication_time
        #print 'cost_hose_replacement_taimi: ' + str(cost_hose_replacement_taimi)
        
        #total cost for taimi
        total_cost_taimi = total_one_inch_swivel_taimi_cost + total_three_quart_swivel_taimi_cost + cost_downtime_caused_swivel_taimi + cost_oil_leak_caused_swivel_taimi + cost_hose_replacement_taimi
        #print 'total_cost_taimi: ' + str(total_cost_taimi)
        
        save_money_6000_hours = total_cost_competitor - total_cost_taimi
        
        number_of_year = float(6000) / float(hours_worked)
        save_money_by_year = save_money_6000_hours / number_of_year


        return render_to_response('results_calculator.html', {'save_money_6000_hours': save_money_6000_hours, 
                                                              'number_of_year': number_of_year, 
                                                              'save_money_by_year': save_money_by_year,
                                                              'hours_worked': hours_worked,
                                                              'dollar_sign': dollar_sign}, context_instance=RequestContext(request))# Create your views here.
        
        
        
    return render_to_response('taimi_calculator.html', {}, context_instance=RequestContext(request))
