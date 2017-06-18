from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='group-index'),
    url(r'^(?P<group_number>[0-9]+)/$', views.detail, name='group-detail')
]
