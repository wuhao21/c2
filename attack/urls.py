from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<attacker>[0-9A-Za-z]+)/(?P<whom>.*)', views.attack_post, name='attack-post'),
    url(r'^(?P<aid>[0-9]+)$', views.detail, name='attack-detail'),
]
