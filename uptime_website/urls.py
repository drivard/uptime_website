from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('uptimes.views',
    # home page
    url(r'^$', 'index'),
    # page about the project goal
    url(r'^about/', 'about'),
    # page to contact support
    url(r'^contact/', 'contact'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'uptime_website.views.home', name='home'),
    # url(r'^uptime_website/', include('uptime_website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
