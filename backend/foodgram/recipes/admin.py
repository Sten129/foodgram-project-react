# from django.contrib import admin
# from api.models import Recipe, Ingredient, Follow, Tag, IngredientInRecipe
#
#
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'tags',
#         'author',
#         'ingredients',
#         'is_favorited',
#         'is_in_shopping_cart',
#         'image',
#         'description',
#         'cooking_time'
#     )
#     empty_value_display = '-пусто-'
#     search_fields = (
#         'tags',
#         'author',
#         'is_favorited',
#         'is_in_shopping_cart',
#         'cooking_time'
#     )
#
#
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'measurement_unit')
#     empty_value_display = '-пусто-'
#     search_fields = ('id', 'name')
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('title', 'hexcode_color', "slug")
#     empty_value_display = '-пусто-'
#     search_fields = ('title',)
#
#
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(Tag, TagAdmin)
#
# # Register your models here.
