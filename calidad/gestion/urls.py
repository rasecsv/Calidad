from django.conf.urls import url

from . import models

urlpatterns = [
    url(r'^$', views.user, name='user'),
]