from django.contrib import admin
from .models import Recipe





class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tags',
        'author',
        'ingredients',
        'is_favorited',
        'is_in_shopping_cart',
        'image',
        'description',
        'cooking_time'
    )
    empty_value_display = '-пусто-'
    search_fields = (
        'tags',
        'author',
        'is_favorited',
        'is_in_shopping_cart',
        'cooking_time'
    )

admin.site.register(Recipe, RecipeAdmin)

# Register your models here.
