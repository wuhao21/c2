from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<aid>[0-9]+)/$', views.detail, name='attack-detail')
]
