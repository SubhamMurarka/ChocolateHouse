from django.urls import path
from . import views

urlpatterns = [
    # Seasonal Flavors
    path('seasonal_flavors/', views.seasonal_flavors, name='seasonal_flavors'),
    path('seasonal_flavors/update/<int:pk>/', views.update_seasonal_flavor, name='update_seasonal_flavor'),
    path('seasonal_flavors/delete/<int:pk>/', views.delete_seasonal_flavor, name='delete_seasonal_flavor'),
    
    # Ingredients
    path('ingredients/', views.ingredients, name='ingredients'),
    path('ingredients/update/<int:pk>/', views.update_ingredient, name='update_ingredient'),
    path('ingredients/delete/<int:pk>/', views.delete_ingredient, name='delete_ingredient'),
    
    # Customer Suggestions
    path('customer_suggestions/', views.customer_suggestions, name='customer_suggestions'),
    path('customer_suggestions/update/<int:pk>/', views.update_customer_suggestion, name='update_customer_suggestion'),
    path('customer_suggestions/delete/<int:pk>/', views.delete_customer_suggestion, name='delete_customer_suggestion'),
]
