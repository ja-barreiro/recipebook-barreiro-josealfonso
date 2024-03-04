from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path('recipes/list', list_view, name='list-view'),
    path('recipe/<int:recipe_id>', detail_view, name='detail-view'),
]

app_name = "ledger"