from django.urls import path
from .views import RecipeListView, RecipeCreateView, RecipeDetailView, RecipeDeleteView, IngredientCreateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('ingredient/add/', IngredientCreateView.as_view(), name='ingredient-add'),
]
