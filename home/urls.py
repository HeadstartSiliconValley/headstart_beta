from django.conf.urls import url
from django.contrib.auth.views import login

from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'home'

urlpatterns = [

	url(r'^$', login, {'template_name': 'home/index.html'}),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name = 'login'),
    url(r'^logout/$', views.logout_page , name='logout'),
    url(r'^personal/$', views.personal , name='personal'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)