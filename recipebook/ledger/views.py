from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeIngredient

def list_view(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'ledger/list.html', ctx)


def detail_view(request, recipe_id):
    ctx = { 'recipe', Recipe.objects.get(id=id) }
    return render(request, 'ledger/recipe_detail.html', ctx)