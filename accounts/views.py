from django.shortcuts import render_to_response
from django.template import RequestContext as rc
from django.contrib.auth.decorators import login_required


@login_required
def settings(request):
    '''
    '''
    
    return render_to_response(
                "settings.html", 
                locals(),
                context_instance=rc(request))