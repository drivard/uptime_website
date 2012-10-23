from django.shortcuts import render_to_response
from django.template import RequestContext as rc
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def read(request):
    '''
    
    This view will get the JSON dataset push by the agent and will try
    to associate it to a registered member having the computer in his
    list and update the information of the computer uptime.
    
    '''
    
    return render_to_response(
                "read.html", 
                locals(),
                context_instance=rc(request))


def index(request):
    '''
    
    This view doesn't do much, it only displays a error message 
    explaining that the API can only be called by the agent.
    
    '''
    
    return render_to_response(
                "api/index.html", 
                locals(),
                context_instance=rc(request))