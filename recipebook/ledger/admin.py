from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)