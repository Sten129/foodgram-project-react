from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredient(models.Model):
    # обращаемся к базе через foreign key
    # name = models.CharField(max_length=200, help_text='Название ингредиента')
    id = models.IntegerField(verbose_name='Уникальный id', primary_key=True)
    name = models.CharField(verbose_name='Название ингредиента', max_length=200)
    quantity = models.IntegerField()
    measurement_unit = models.CharField(max_length=200)
    # recipe = models.ForeignKey(Recipe)
    # amount

    pass


class Tag(models.Model):
    title = models.CharField(max_length=200)
    hexcode = models.IntegerField()
    slug = models.SlugField()
    pass


class Recipe(models.Model):
    id = models.IntegerField(verbose_name='Уникальный id', primary_key=True)
    tags = models.ForeignKey(Tag, verbose_name='Список тегов', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='author',
        on_delete=models.CASCADE,
        related_name='recipes')
    ingredients = models.ForeignKey(
        Ingredient,
        verbose_name='Список ингредиентов',
        null=False,
        on_delete=models.CASCADE
    )
    is_favorited = models.BooleanField(verbose_name='Находится ли в избранном')
    is_in_shopping_cart = models.BooleanField(verbose_name='Находится ли в корзине')
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
    # ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # ingredients = models.ManyToManyField(Ingredient)
    cooking_time = models.IntegerField(verbose_name='Время приготовления в минутах')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Follower',
        help_text='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower')
    author = models.ForeignKey(
        User,
        verbose_name='author',
        help_text='Автор',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], name='unique_follow'),
        ]

    pass

# Create your models here.
