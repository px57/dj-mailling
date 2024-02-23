"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'unsubscribe/', 
        views.unsubscribe, 
        name='mailling__unsubscribe'
    ),
    path(
        'subscribe/', 
        views.unsubscribe, 
        name='mailling__subscribe'
    ),
]