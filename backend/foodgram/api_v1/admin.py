from api_v1.models import Follow, Ingredient, IngredientInRecipe, IsFavorited, IsInShoppingCart, Recipe, Tag
from django.contrib import admin


class IngredientInline(admin.TabularInline):
    model = IngredientInRecipe
    insert_after = 'cooking_time'


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
    inlines = [
        IngredientInline,

    ]


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


class TagInline(admin.TabularInline):
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
