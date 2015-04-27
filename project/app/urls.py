from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from app import views

urlpatterns = patterns('',
    url(r'^home/$', views.home, name='home'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^$', views.home, name='home2'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^reginfo/$', views.reginfo, name='reginfo'),

)
