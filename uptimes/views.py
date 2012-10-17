from django.shortcuts import render_to_response
from django.template import RequestContext as rc

def index(request):
    '''
    '''
    template = 'base.html'
    test = 'hello world!'
    
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))
                                

def contact(request):
    '''
    '''
    template = 'base.html'
    author = 'Dominick Rivard'
    
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))
                

ABOUT_TEXT = '''I made that project because I wanted to prove myself that
I was able to move a website project from ground zero to a production website.

I also love working and developing with Python, Django and Linux. That project
was a great deal of learning many new little things that I could re-use later.

I made this project open source on github in the hope that peoples will contribute
to the site and make it a better site.
'''

                
def about(request):
    '''
    '''
    template = 'base.html'
    about_text = ABOUT_TEXT
    
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))
                
                
def getstarted(request):
    '''
    '''
    template = 'base.html'
    
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))