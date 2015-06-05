#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import connection, transaction
from django.conf import settings
from django.utils.translation import ugettext as _
from autoslug import AutoSlugField
import datetime
from ckeditor.fields import RichTextField
from cms.models import CMSPlugin

SECTION_CHOICES = (
    ('1', 'Live swivels'),
    ('2', 'Swivel products'),
)

class Testimonies(models.Model):
    date = models.DateField(default=datetime.date.today)
    nom = models.CharField(max_length=150)
    poste = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='nom', unique=True)
    image = models.FileField(upload_to='testimonies/')
    section = models.CharField(max_length=200,
                               choices=SECTION_CHOICES,
                               default=0)
    class Translation:
        description = models.TextField(blank = True, null = True)
        poste = models.CharField(max_length=150, null = True, blank = True)
    
    
    def __unicode__(self):
        return self.nom

class TestimoniesPlugin(CMSPlugin):
    section = models.CharField(max_length=200,
                               choices=SECTION_CHOICES,
                               default=0)
    @property
    def testimonies(self):
        return Testimonies.objects.filter(section = self.section)
