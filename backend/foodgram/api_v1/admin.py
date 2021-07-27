from django.contrib import admin

from django.contrib import admin
from api_v1.models import Recipe, Ingredient, Follow, Tag, IngredientInRecipe, IsFavorited, IsInShoppingCart


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tags',
        'author',
        'ingredients',
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


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    empty_value_display = '-пусто-'
    search_fields = ('id', 'name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'hexcode_color', "slug")
    empty_value_display = '-пусто-'
    search_fields = ('title',)

class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'amount')
    empty_value_display = '-пусто-'
    search_fields = ('ingredient',)
    pass

class IsFavoritedAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    empty_value_display = '-пусто-'
    search_fields = ('user', 'recipe')

    pass

class IsInShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    empty_value_display = '-пусто-'
    search_fields = ('user', 'recipe')
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
admin.site.register(IsFavorited, IsFavoritedAdmin)
admin.site.register(IsInShoppingCart, IsInShoppingCartAdmin)