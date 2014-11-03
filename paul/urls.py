from django.conf.urls import patterns, include, url
from paul.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #HOME AND ADMIN
    url(r'^$', 'paul.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    
    #AUTHENTICATION
    (r'^login/$', 'paul.views.login'),
    (r'^auth/$', 'paul.views.auth_view'),
    (r'^logout/$', 'paul.views.logout'),
    (r'^logged_in/$', 'paul.views.logged_in'),
    (r'^invalid/$', 'paul.views.invalid_login'),
    
    #REGISTRATION
    (r'^register/$', 'paul.views.register_user'),
    (r'^register_success/$', 'paul.views.register_success'),
)