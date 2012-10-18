import datetime
from django import template

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