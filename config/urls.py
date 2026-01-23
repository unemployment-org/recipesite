from django.contrib import admin
from django.urls import path, include
# Добавляем profile_view в импорты:
from recipes.views import recipe_list, recipe_create, recipe_detail, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_list, name='home'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/new/', recipe_create, name='recipe_create'),

    # НОВАЯ ССЫЛКА НА ПРОФИЛЬ:
    path('accounts/profile/', profile_view, name='profile'),

    path('accounts/', include('django.contrib.auth.urls')),
]