from django.db import models
from django.contrib.auth.models import User  # Импортируем пользователя
from django.core.validators import MaxValueValidator, MinValueValidator  # Для оценки 1-5


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField(default="...")
    ingredients = models.TextField(default="...")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')

    # --- НОВЫЕ ПОЛЯ ---
    # Кто добавил рецепт (если удалим юзера, рецепт останется)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Простое текстовое поле для тегов (например: "Острое, Быстро")
    tags = models.CharField(max_length=200, blank=True, help_text="Введите теги через запятую")

    def __str__(self): return self.title


# --- НОВАЯ МОДЕЛЬ ---
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Оценка от 1 до 5
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"Comment by {self.author} on {self.recipe}"