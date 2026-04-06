from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, CommentForm
from django.db.models import Q  # <--- Добавь этот импорт в самом верху!
from rest_framework import generics
from .serializers import RecipeSerializer

# Список рецептов
def recipe_list(request):
    search_query = request.GET.get('search', '')  # Получаем текст из строки поиска

    if search_query:
        # Ищем, где название ИЛИ описание содержит текст
        recipes = Recipe.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(tags__icontains=search_query)
        ).order_by('-created_at')
    else:
        recipes = Recipe.objects.all().order_by('-created_at')

    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'search_query': search_query  # Передаем обратно, чтобы оставить текст в поле
    })

# Детальный просмотр рецепта + Комментарии
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'comments': comments,
        'form': form
    })


# Создание рецепта (только для вошедших)
@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

# ... ваши импорты (убедитесь, что User импортирован)
# Если нет, добавьте сверху: from django.contrib.auth.models import User

@login_required
def profile_view(request):
    # Показываем только рецепты текущего пользователя
    user_recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'recipes/profile.html', {'recipes': user_recipes})

class RecipeListCreateAPI(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer