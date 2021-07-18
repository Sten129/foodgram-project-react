from django.shortcuts import get_object_or_404
from rest_framework import serializers

from backend.foodgram.recipes.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    pass