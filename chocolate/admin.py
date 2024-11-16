from django.contrib import admin
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion

# Registering models
admin.site.register(SeasonalFlavor)
admin.site.register(Ingredient)
admin.site.register(CustomerSuggestion)
