from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^forum/', include('forum.urls')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/', include('registration.urls')),
)
