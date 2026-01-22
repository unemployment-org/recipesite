from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    # Берем все рецепты из базы
    recipes = Recipe.objects.all().order_by('-created_at')
    # Отдаем их в шаблон (html)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

# --- API VIEWS ---
from rest_framework import generics
from .serializers import RecipeSerializer

class RecipeListCreateAPI(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer