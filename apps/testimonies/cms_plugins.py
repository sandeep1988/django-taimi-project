from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from testimonies.models import TestimoniesPlugin as Testimonies
from django.utils.translation import ugettext as _

class TestimoniesPlugin(CMSPluginBase):
    model = Testimonies # Model where data about this plugin is saved
    name = _("Testimonies List") # Name of the plugin
    render_template = "testimonies_plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(TestimoniesPlugin) # register the plugin
