from django.shortcuts import render
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion

# View for Seasonal Flavors
def seasonal_flavors(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'chocolate/seasonal_flavors.html', {'flavors': flavors})

# View for Ingredients
def ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'chocolate/ingredients.html', {'ingredients': ingredients})

# View for Customer Suggestions
def customer_suggestions(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        flavor_suggestion = request.POST.get('flavor_suggestion')
        allergy_concerns = request.POST.get('allergy_concerns')
        
        # Save the suggestion to the database
        CustomerSuggestion.objects.create(
            customer_name=customer_name,
            flavor_suggestion=flavor_suggestion,
            allergy_concerns=allergy_concerns
        )
        message = "Thank you for your suggestion!"
        return render(request, 'chocolate/customer_suggestions.html', {'message': message})
    
    return render(request, 'chocolate/customer_suggestions.html')
