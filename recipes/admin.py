from django.contrib import admin
from .models import Category, Recipe

# Регистрируем категорию просто (стандартный вид)
admin.site.register(Category)

# Настраиваем вид для рецептов (таблички, поиск, фильтры)
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at') # Столбцы в списке
    list_filter = ('category',)                        # Фильтр справа (по категориям)
    search_fields = ('title', 'description')           # Строка поиска вверху