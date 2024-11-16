from django.shortcuts import render, redirect, get_object_or_404
from .models import SeasonalFlavor

# List and Create
def seasonal_flavors(request):
    if request.method == 'POST':
        # Create a new seasonal flavor
        name = request.POST.get('name')
        description = request.POST.get('description')
        SeasonalFlavor.objects.create(name=name, description=description)
        return redirect('seasonal_flavors')

    flavors = SeasonalFlavor.objects.all()
    return render(request, 'chocolate/seasonal_flavors.html', {'flavors': flavors})

# Update
def update_seasonal_flavor(request, pk):
    flavor = get_object_or_404(SeasonalFlavor, pk=pk)
    if request.method == 'POST':
        flavor.name = request.POST.get('name')
        flavor.description = request.POST.get('description')
        flavor.save()
        return redirect('seasonal_flavors')

    return render(request, 'chocolate/update_seasonal_flavor.html', {'flavor': flavor})

# Delete
def delete_seasonal_flavor(request, pk):
    flavor = get_object_or_404(SeasonalFlavor, pk=pk)
    flavor.delete()
    return redirect('seasonal_flavors')

from .models import Ingredient

# List and Create
def ingredients(request):
    if request.method == 'POST':
        # Add a new ingredient
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        Ingredient.objects.create(name=name, quantity=quantity, unit=unit)
        return redirect('ingredients')

    ingredients = Ingredient.objects.all()
    return render(request, 'chocolate/ingredients.html', {'ingredients': ingredients})

# Update
def update_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.name = request.POST.get('name')
        ingredient.quantity = request.POST.get('quantity')
        ingredient.unit = request.POST.get('unit')
        ingredient.save()
        return redirect('ingredients')

    return render(request, 'chocolate/update_ingredient.html', {'ingredient': ingredient})

# Delete
def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    ingredient.delete()
    return redirect('ingredients')

from .models import CustomerSuggestion

# List and Create
def customer_suggestions(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        flavor_suggestion = request.POST.get('flavor_suggestion')
        allergy_concerns = request.POST.get('allergy_concerns')
        CustomerSuggestion.objects.create(
            customer_name=customer_name,
            flavor_suggestion=flavor_suggestion,
            allergy_concerns=allergy_concerns
        )
        return redirect('customer_suggestions')

    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'chocolate/customer_suggestions.html', {'suggestions': suggestions})

# Update
def update_customer_suggestion(request, pk):
    suggestion = get_object_or_404(CustomerSuggestion, pk=pk)
    if request.method == 'POST':
        suggestion.customer_name = request.POST.get('customer_name')
        suggestion.flavor_suggestion = request.POST.get('flavor_suggestion')
        suggestion.allergy_concerns = request.POST.get('allergy_concerns')
        suggestion.save()
        return redirect('customer_suggestions')

    return render(request, 'chocolate/update_customer_suggestion.html', {'suggestion': suggestion})

# Delete
def delete_customer_suggestion(request, pk):
    suggestion = get_object_or_404(CustomerSuggestion, pk=pk)
    suggestion.delete()
    return redirect('customer_suggestions')
