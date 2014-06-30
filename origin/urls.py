from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'origin.views.home', name='home'),
<<<<<<< HEAD
      url(r'^blog/', include('blog.urls')),
      url(r'^admin/', include(admin.site.urls)),
=======
    url(r'^$', include('website.urls', namespace='website')),
    url(r'^admin/', include(admin.site.urls)),
>>>>>>> 714493606e531bfde9c05b91f4d374df80fb4fa1
)
