from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^forum/', include('forum.urls')),
	url(r'^theater/', 'theater.views.index'),
	url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/', include('registration.urls')),
)

if settings.DEBUG:
  #static files (images, css, javascript, etc.)
  urlpatterns += patterns('', (r'^media/(?P<path>.*)', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT}))
