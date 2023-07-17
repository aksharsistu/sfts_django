from django.urls import path
from . import views

urlpatterns = [
    # Line URLs
    path('line/get/', views.line_get, name='line_get'),
    path('line/set/', views.line_set, name='line_set'),
    path('line/delete/', views.line_delete, name='line_delete'),

    # Product URLs
    path('product/get/', views.product_get, name='product_get'),
    path('product/set/', views.product_set, name='product_set'),
    path('product/delete/', views.product_delete, name='product_delete'),

    # Rejection URLs
    path('rejection/get/', views.rejection_get, name='rejection_get'),
    path('rejection/set/', views.rejection_set, name='rejection_set'),
    path('rejection/delete/', views.rejection_delete, name='rejection_delete'),

    # Rework URLs
    path('rework/get/', views.rework_get, name='rework_get'),
    path('rework/set/', views.rework_set, name='rework_set'),
    path('rework/delete/', views.rework_delete, name='rework_delete'),
]
