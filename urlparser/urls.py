from django.conf.urls import patterns, url

from urlparser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^images$', views.images, name='images'),
    url(r'^modelform_example/(?P<image_id>\d+)/$', views.modelform_example, name='modelform_example_args'),
    url(r'^modelform_example/$', views.modelform_example, name='modelform_example'),
)
