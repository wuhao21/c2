from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<gid>[0-9]+\-[1-4])/$', views.detail, name='group-detail'),
    url(r'^g/(?P<gid>[0-9]+\-[1-4])/$', views.generate, name='group-generate'),
    url(r'^r/(?P<gid>[0-9]+\-[1-4])/$', views.readme, name='group-readme'),
]
