from django.shortcuts import render_to_response
from django.http import  Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, Context
from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory
from django.views.decorators.csrf import csrf_protect
from django.utils.functional import curry


def index(request):
    c = Context({
        'user' : request.user,
        })
    return render_to_response('weather/index.html',c,context_instance=RequestContext(request))

def currentweather(request):


    t = 'scheduling/projects.html'
    c = Context({
        'user' : request.user,
#        'project_list': project_list,
#        'project_form': project_edit_form,
#        'filter_form': project_filter_form,
#        'permission_set': permission_set,
#        'proj_status':filter_project_status,
        })
    return render_to_response(t,c,context_instance=RequestContext(request))
