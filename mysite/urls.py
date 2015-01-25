from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.index', name='home'),
    url(r'^imgur/$', 'mysite.views.imgur', name='home'),
    url(r'^upload/$', 'mysite.views.upload', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^urlparser/', include('urlparser.urls', namespace='urlparser')),
)