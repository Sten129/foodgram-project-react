from django.db import models

from foodgram.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Ingredient(models.Model):
    # id = models.IntegerField(verbose_name='Уникальный id', primary_key=True, db_index=True)
    # id = models.IntegerField(verbose_name='Уникальный id', primary_key=True, db_index=True)
    name = models.CharField(verbose_name='Название ингредиента', max_length=200)
    measurement_unit = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient',
                                   verbose_name='Ингредиент в рецепте')
    amount = models.PositiveSmallIntegerField(null=True, verbose_name='Количество ингредиента в рецепте')

    class Meta:
        verbose_name = 'Количество ингредиента в рецепте'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    title = models.CharField(max_length=200)
    hexcode_color = models.CharField(default='#ffffff', max_length=50, verbose_name='Цвет')
    slug = models.SlugField(null=False, unique=False, help_text='URL')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'


class Recipe(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    tags = models.ForeignKey(Tag, verbose_name='Список тегов', on_delete=models.CASCADE, related_name='tags')
    author = models.ForeignKey(AUTH_USER_MODEL,
                               verbose_name='author',
                               on_delete=models.CASCADE,
                               related_name='recipes')
    ingredients = models.ForeignKey(IngredientInRecipe, related_name='ingredients', on_delete=models.CASCADE)

    name = models.CharField(
        max_length=200,
        null=False,
        help_text='Название'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipes/',
        null=False,
        help_text='Загрузите изображение'
    )  # проверить
    description = models.TextField(
        verbose_name='Текст',
        null=False,
        help_text='Здесь будет текст Вашего рецепта'
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    cooking_time = models.PositiveSmallIntegerField(verbose_name='Время приготовления в минутах')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name
    #   проверить!!!


class Follow(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name='Follower',
        help_text='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower')
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name='author',
        help_text='Автор',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], name='unique_follow'),
        ]


class IsFavorited(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Любитель', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, help_text='Рецепт', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'], name='uniqiue_favorited')
        ]


class IsInShoppingCart(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Покупатель', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, help_text='Рецепт', on_delete=models.CASCADE, )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'], name='uniqiue_shopping')
        ]
