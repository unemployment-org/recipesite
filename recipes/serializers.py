from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'category_name', 'created_at']