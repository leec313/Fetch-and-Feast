from django.urls import path
from . import views


urlpatterns = [
     path('', views.all_products, name='products'),
     path('<int:product_id>/', views.product_detail, name='product_detail'),
     path('manage-products/', views.manage_products, name='manage_products'),
     path('bulk_delete/', views.bulk_delete_products,
          name='bulk_delete_products'),
     path('add_category/', views.add_category,
          name='add_category'),
     path('add/', views.add_product, name='add_product'),
     path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
     path('delete/<int:product_id>/',
          views.delete_product, name='delete_product'),
     path('rating/<int:pk>/delete/',
          views.RatingDeleteView.as_view(), name='rating_delete'),
     path('rating/<int:pk>/edit/',
          views.RatingUpdateView.as_view(), name='rating_edit'),
]
