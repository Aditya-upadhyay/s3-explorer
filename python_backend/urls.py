from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 's3.views.home', name='home' ),
    url(r'^bucket/*', 's3.views.bucket', name='bucket'),
    url(r'^clear/', 's3.views.clear', name='clear_session'),
)
