from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site
from django.utils import translation
from django.shortcuts import redirect

class LangRedirMiddleware(object):  
    def process_view(self, request, view_func, view_args, view_kwargs):
        host = request.build_absolute_uri().split('/')[2]

        if host == "en.taimi.ca" or host == "localhost:8000":
            if not request.LANGUAGE_CODE == 'en':
                # redirection vers l'ancien site
                url = "http://taimi.ca/" + request.LANGUAGE_CODE
                return redirect(url)
            else:
                try:
                    lang = request.build_absolute_uri().split('/')[3]
                    if lang == 'fr' or lang == 'es':
                        url = "http://taimi.ca/" + lang
                        return redirect(url)
                    
                except:
                    pass
                
        elif request.LANGUAGE_CODE == 'en':
            url = "http://en.taimi.ca/" + request.LANGUAGE_CODE + request.get_full_path()
            return redirect(url)
            
        return None
