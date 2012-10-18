from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()


'''

The website URLs

'''
urlpatterns = patterns('uptimes.views',
    # home page
    url(r'^$', 'index'),
    # page about the project goal
    url(r'^about/', 'about'),
    # page to contact support
    url(r'^contact/', 'contact'),
    # how to instruction
    url(r'^getstarted/', 'getstarted'),
    # humans.txt
    url(r'^humans\.txt$', direct_to_template,
        {'template': 'humans.txt', 'mimetype': 'text/plain'}),
    # robots.txt
    url(r'^robots\.txt$', direct_to_template,
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)


'''

Django-registration plugins

'''
urlpatterns += patterns('', 
    # registration urls
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)


'''

Admin URLs

'''
urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'uptime_website.views.home', name='home'),
    # url(r'^uptime_website/', include('uptime_website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
