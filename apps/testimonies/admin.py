from django.contrib.admin import site, ModelAdmin
from testimonies.models import Testimonies
from multilingual.admin import MultilingualModelAdmin

class TestimoniesAdmin(MultilingualModelAdmin):
    pass
    

site.register(Testimonies, TestimoniesAdmin)


