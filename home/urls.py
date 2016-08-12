from django.conf.urls import url
from django.contrib.auth.views import login

from . import views


app_name = 'home'

urlpatterns = [

	url(r'^$', login, {'template_name': 'home/index.html'}),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name = 'login'),
    url(r'^logout/$', views.logout_page , name='logout'),

    #  url(r'^home/$', views.home),
    #  url(r'^register/success/$', views.register_success , name = 'success'),
    #url(r'^$', auth_views.login, {'home': 'home/index.html'}),
]
