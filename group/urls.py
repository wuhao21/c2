from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<gid>[0-9]+)/$', views.detail, name='group-detail')
]
