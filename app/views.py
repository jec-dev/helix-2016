from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required

def landing_view(request):
    name = 'Foo Bar'
    context = RequestContext(request)
    t = get_template('index.html')
    return render_to_response('landing.html', context)

