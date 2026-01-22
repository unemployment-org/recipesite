from django.contrib import admin
from django.urls import path
# ВНИМАНИЕ: Добавьте RecipeListCreateAPI в конец этой строки через запятую
from recipes.views import recipe_list, RecipeListCreateAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_list, name='home'),
    path('api/recipes/', RecipeListCreateAPI.as_view(), name='recipe_api'),
]