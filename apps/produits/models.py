#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db import connection, transaction
from django.conf import settings
from django.utils.translation import ugettext as _
from autoslug import AutoSlugField
import datetime
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from cms.models import Page

class Category(models.Model):

	associated_page = models.ForeignKey(Page)
	slug = AutoSlugField(populate_from='title', unique=True, blank = True, null = True)
	image = models.ImageField(upload_to = 'media/categories/', null = True, blank = True)
	image2 = models.ImageField(upload_to = 'media/categories/', null = True, blank = True)
	
	class Translation:
		title = models.CharField(max_length=200)
		description = models.TextField(null=True, blank=True, default=" ")
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('produits.views.getSubCats', args=[self.slug])
    
class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    slug = AutoSlugField(populate_from='title', unique=True, blank = True, null = True)
    image = models.ImageField(upload_to = 'media/subcategories/', null = True, blank = True)
    order = models.IntegerField(default=0)
    
    def get_url(self):
        return self.category.slug + '/' + self.slug + '/' 
    
    class Translation:
        description = models.TextField(null=True, blank=True, default=" ")
        
    def __unicode__(self):
        return self.title
    
class Product(models.Model):
    part_no = models.CharField(max_length=30)
    reference = models.CharField(max_length=250, null=True, blank=True)
    a = models.CharField(max_length=30, null=True, blank=True)
    b = models.CharField(max_length=30, null=True, blank=True)
    c = models.CharField(max_length=30, null=True, blank=True)
    d = models.CharField(max_length=30, null=True, blank=True)
    p1 = models.CharField(max_length=30, null=True, blank=True)
    p2 = models.CharField(max_length=30, null=True, blank=True)
    p3 = models.CharField(max_length=30, null=True, blank=True)
    h1 = models.CharField(max_length=30, null=True, blank=True)
    h2 = models.CharField(max_length=30, null=True, blank=True)
    seal_kit = models.CharField(max_length=30, null=True, blank=True)
    ports = models.CharField(max_length=150, null=True, blank=True)
    weight = models.CharField(max_length=150, null=True, blank=True)
    online_video = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to = 'media/produits/', null = True, blank = True)
    
    subcategory = models.ForeignKey(SubCategory)
    def __unicode__(self):
        return self.part_no
    def category(self):
        return self.subcategory.category
