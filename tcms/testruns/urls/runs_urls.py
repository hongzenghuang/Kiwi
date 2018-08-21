# -*- coding: utf-8 -*-

from django.conf.urls import url
from .. import views

urlpatterns = [
    url(r'^$', views.get_all, name='testruns-all'),
    url(r'^ajax/$', views.ajax_search, name='testruns-ajax_search'),
]
