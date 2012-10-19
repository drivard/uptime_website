import datetime
from django import template
from django.contrib.sites.models import Site

'''

This template tags helps in building the copyright statement dynamically.

'''

register = template.Library()


class YearNode(template.Node):
    def __init__(self):
        self.year = datetime.datetime.now().year

        
    def render(self, context):        
        return self.year

        
@register.tag
def year(parser, token):
    return YearNode()

    
class DomainNode(template.Node):
    def __init__(self):
        current_site = Site.objects.get_current()
        self.site = current_site.name

        
    def render(self, context):        
        return self.site

        
@register.tag
def domain(parser, token):
    return DomainNode()