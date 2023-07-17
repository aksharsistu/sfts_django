from django.urls import path
from process import views

urlpatterns = [
    path('create/', views.create),
    path('get/', views.get),
    path('card/', views.card),
    path('delete/', views.delete)
]
