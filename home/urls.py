from django.urls import path
from . import views

urlpatterns = [
    path('subscribe_newsletter/', views.subscribe_newsletter,
         name='subscribe_newsletter'),
    path('unsubscribe/', views.unsubscribe_newsletter,
         name='unsubscribe_newsletter'),
    path('', views.index, name='home')
]
