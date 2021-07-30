from django.forms import ModelForm
from django import forms
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model=Recipe
        fields = ['tags', 'author',  'name', 'image', 'text', 'cooking_time' ]