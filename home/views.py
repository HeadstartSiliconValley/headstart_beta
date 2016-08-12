from django.shortcuts import render

from home.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from accounts.models import CustomUser
 


def index(request):
	return render(request,'home/login.html', 
            { 'user': request.user }
         )

'''
Login
'''

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
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
            photo = request.FILES['image']
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
def personal(request):
    return render_to_response(
        'home/personal.html',
    { 'user': request.user }
    )
