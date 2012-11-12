from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^$', 'example.common.views.demo', name="demo"),
)
