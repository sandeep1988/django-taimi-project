# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from django.core.validators import validate_email
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.urlresolvers import reverse
 
class SubscribeForm(forms.Form):
    guid = forms.CharField(max_length=400, 
                     required=False,
                     widget=forms.HiddenInput())
    
    firstname = forms.CharField(
        label = _("First name:"),
        max_length = 255,
        required = True,
    )
    
    lastname = forms.CharField(
        label = _("Last name:"),
        max_length = 255,
        required = True,
    )

    email = forms.CharField(
        label = _("Email:"),
        max_length = 255,
        required = True,
    )
    
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_id = 'subscribeForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('nouvelles.views.news', args=[]) + '#subscribeForm'

        self.helper.add_input(Submit('subscribe', _('Subscribe'), css_class='btn btn-orange btn-large'))

    def clean_email(self):
        data = self.cleaned_data['email']
        try :
            validate_email(data)
            
        except:
            raise forms.ValidationError(_("Invalid email!"))
        