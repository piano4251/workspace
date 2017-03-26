'''
Created on 2017. 3. 12.

@author: YG
'''

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/$',views.areas)
]