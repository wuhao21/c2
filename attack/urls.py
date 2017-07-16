from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<aid>[0-9]+)$', views.detail, name='attack-detail'),
    url(r'^post/(?P<whom>.*)', views.attack_post, name='attack-post'),
    url(r'^history/', views.history, name='history'),
    url(r'^', views.list, name='attack-list'),
]
