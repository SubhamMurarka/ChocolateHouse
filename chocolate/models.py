from django.db import models

class SeasonalFlavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    flavor_suggestion = models.CharField(max_length=200)
    allergy_concerns = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Suggestion by {self.customer_name}: {self.flavor_suggestion}"

