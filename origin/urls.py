from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'origin.views.home', name='home'),
    url(r'^$', include('website.urls', namespace='website')),
    url(r'^admin/', include(admin.site.urls)),
)
