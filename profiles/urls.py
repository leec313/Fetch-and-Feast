from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
