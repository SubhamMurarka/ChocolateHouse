from django.urls import path
from . import views

urlpatterns = [
    path('flavors/', views.seasonal_flavors, name='seasonal_flavors'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('suggestions/', views.customer_suggestions, name='customer_suggestions'),
]
