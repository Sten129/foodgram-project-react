from django.contrib import admin

from django.contrib import admin
from api_v1.models import Recipe, Ingredient, Follow, Tag, IngredientInRecipe, IsFavorited, IsInShoppingCart


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'description',
        'image',
        'cooking_time'
    )
    list_filter = ('id',)
    empty_value_display = '-пусто-'
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('id',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'hexcode_color', "slug")
    empty_value_display = '-пусто-'
    search_fields = ('title',)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
    empty_value_display = '-пусто-'
    search_fields = ('ingredient',)

class IngredientInline(admin.TabularInline):
    """
    Inline to show ingredients on recipe page.
    """
    model = IngredientInRecipe
    insert_after = 'cooking_time'

class TagInline(admin.TabularInline):
    """
    Inline to show ingredients on recipe page.
    """
    model = Recipe.tags.through
    insert_after = 'image'


class IsFavoritedAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    empty_value_display = '-пусто-'
    search_fields = ('recipe',)


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
