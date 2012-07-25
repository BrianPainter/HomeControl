from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from djangorestframework.views import ListOrCreateModelView, InstanceModelView

from rainbarrel.resources import WaterLevelResource

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HomeControl.views.home', name='home'),
    # url(r'^HomeControl/', include('HomeControl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (
        r"^$",
        "django.views.generic.simple.direct_to_template",
            {'template': "weather/index.html"},
        ),


    (r'^$','weather.views.index'),
    (r'^weather/$','weather.views.currentweather'),
    (r'^sprinklers/log/$','sprinklers.views.sprinklerlog'),
    (r'^rainbarrel/level/$','rainbarrel.views.graphicalview'),


    url(r'^rainbarrel/$', ListOrCreateModelView.as_view(resource=WaterLevelResource),name='rainbarrel-root'),
#    url(r'^(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=WaterLevelResource),name='rainbarrel'),

)
