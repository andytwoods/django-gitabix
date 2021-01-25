# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_gitabix'
urlpatterns = [
    url(r'gitabix', views.action, name='gitabix-action'),
    ]
