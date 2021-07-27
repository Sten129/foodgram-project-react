# from django.db import models
# from django.contrib.auth import get_user_model
# from django.db import models
#
# User = get_user_model()
#
#
# class Ingredient(models.Model):
#     # обращаемся к базе через foreign key
#     # name = models.CharField(max_length=200, help_text='Название ингредиента')
#     id = models.IntegerField(verbose_name='Уникальный id', primary_key=True)
#     name = models.CharField(verbose_name='Название ингредиента', max_length=200)
#     quantity = models.IntegerField()
#     measurement_unit = models.CharField(max_length=200)
#     # recipe = models.ForeignKey(Recipe)
#     # amount = models.Choices()
#
#     pass
#
#
# class Tag(models.Model):
#     title = models.CharField(max_length=200)
#     # color = models.ColorField()
#     hexcode_color = models.IntegerField()
#     slug = models.SlugField()
#     pass
#
#
# class Recipe(models.Model):
#     id = models.IntegerField(verbose_name='Уникальный id', primary_key=True)
#     tags = models.ForeignKey(Tag, verbose_name='Список тегов', on_delete=models.CASCADE)
#     author = models.ForeignKey(
#         User,
#         verbose_name='author',
#         on_delete=models.CASCADE,
#         related_name='recipes')
#     ingredients = models.ForeignKey(
#         Ingredient,
#         verbose_name='Список ингредиентов',
#         null=False,
#         on_delete=models.CASCADE
#     )
#     is_favorited = models.BooleanField(verbose_name='Находится ли в избранном')
#     is_in_shopping_cart = models.BooleanField(verbose_name='Находится ли в корзине')
#     name = models.CharField(
#         max_length=200,
#         null=False,
#         help_text='Название'
#     )
#     image = models.ImageField(
#         verbose_name='Картинка',
#         upload_to='recipes/',
#         null=False,
#         help_text='Загрузите изображение'
#     )  # проверить
#     description = models.TextField(
#         verbose_name='Текст',
#         null=False,
#         help_text='Здесь будет текст Вашего рецепта'
#     )
#     # ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     # ingredients = models.ManyToManyField(Ingredient)
#     # ingredients = models.Choices(Ingredient)
#     cooking_time = models.IntegerField(verbose_name='Время приготовления в минутах')
#
#     def __str__(self):
#         return self.description[:6]
#     #   проверить!!!
#
#
# class IngredientInRecipe(models.Model):
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient', verbose_name='Ингредиент в рецепте')
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
#     amount = models.IntegerField(null=True, verbose_name='Количество ингредиента в рецепте')
#
#     class Meta:
#         verbose_name = 'Количество ингредиента в рецепте'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return f'{self.ingredient} в {self.recipe}'
#     pass
#
#
# class Follow(models.Model):
#     user = models.ForeignKey(
#         User,
#         verbose_name='Follower',
#         help_text='Подписчик',
#         on_delete=models.CASCADE,
#         related_name='follower')
#     author = models.ForeignKey(
#         User,
#         verbose_name='author',
#         help_text='Автор',
#         on_delete=models.CASCADE,
#         related_name='following'
#     )
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user', 'author'], name='unique_follow'),

#         ]
#
#     pass
#
#
# class IsFavorited(models.Model):
#     user = models.ForeignKey(User, verbose_name='Любитель', on_delete=models.CASCADE, related_name='is_favorited')
#     recipe = models.ForeignKey(Recipe, help_text='Рецепт', on_delete=models.CASCADE, related_name='recipe')
#     pass
#
# class IsInShoppingCart(models.Model):
#     user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE, related_name='buyer')
#     recipe = models.ForeignKey(Recipe, help_text='Рецепт', on_delete=models.CASCADE, related_name='recipe')
#     #ingredient = models.ForeignKey(Ingredient)
#     pass
# # Create your models here.
