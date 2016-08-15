from django.shortcuts import render

from home.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .models import CustomUser
 


def index(request):
	return render(request,'home/index.html', 
            { 'user': request.user }
         )

'''
Login
'''

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )

            CustomUser.objects.create(
            user = user,
            phone = form.cleaned_data['phone'],
            grade = form.cleaned_data['grade'],

            )
            return HttpResponseRedirect('/home')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/home')
 
@login_required
def home(request):
    return render_to_response(
    'login.html',
    { 'user': request.user }
    )
