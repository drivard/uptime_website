from django.shortcuts import render_to_response
from django.template import RequestContext as rc

def index(request):
    '''
    '''
    test = 'hello world! by Dominick'
    template = 'base.html'
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))
                                

def contact(request):
    '''
    '''
    author = 'Dominick Rivard'
    template = 'base.html'
    
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))
                
                
def about(request):
    '''
    '''
    about_text = 'What is the reason for this project'
    template = 'base.html'
    
    return render_to_response(
                template, 
                locals(),
                context_instance=rc(request))