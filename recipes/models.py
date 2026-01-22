from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")
    instructions = models.TextField(verbose_name="Инструкция по приготовлению", default="...")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # Связь: у одного рецепта одна категория, но в категории много рецептов
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes', verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
