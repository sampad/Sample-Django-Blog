from django.conf.urls.defaults import patterns, include, url
from myblog import insta_blog
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^login/',include('insta_blog.urls')),
    url(r'^logged_in/$','insta_blog.views.logged_in_message'),
)
