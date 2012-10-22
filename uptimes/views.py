from django.shortcuts import render_to_response
from django.template import RequestContext as rc

def index(request):
    '''
    '''
    
    return render_to_response(
                "index.html", 
                locals(),
                context_instance=rc(request))
                                

def contact(request):
    '''
    '''
    
    return render_to_response(
                "contact.html", 
                locals(),
                context_instance=rc(request))
                
                
def about(request):
    '''
    '''
    
    return render_to_response(
                "about.html", 
                locals(),
                context_instance=rc(request))
                
                
def getstarted(request):
    '''
    '''
    
    return render_to_response(
                "getstarted.html", 
                locals(),
                context_instance=rc(request))