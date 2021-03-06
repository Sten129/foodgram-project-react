from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента',
        max_length=200
    )
    measurement_unit = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=200)
    hexcode_color = models.CharField(
        default='#ffffff',
        max_length=50,
        verbose_name='Цвет'
    )
    slug = models.SlugField(null=False, unique=False, help_text='URL')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'


class Recipe(models.Model):
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        blank=True,
        null=True,
        verbose_name='Тeги рецепта'
    )
    author = models.ForeignKey(
        User,
        verbose_name='author',
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        null=False,
        through='IngredientInRecipe',
        related_name='ingredients'
    )
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
    )
    text = models.TextField(
        verbose_name='Текст',
        null=False,
        help_text='Здесь будет текст Вашего рецепта'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient',
        verbose_name='Ингредиент в рецепте'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    amount = models.PositiveSmallIntegerField(
        null=True,
        verbose_name='Количество ингредиента в рецепте'
    )

    class Meta:
        verbose_name = 'Количество ингредиента в рецепте'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ingredient} в {self.recipe}'


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='User',
        help_text='Подписчик',
        on_delete=models.CASCADE,
        related_name='subscriber')
    author = models.ForeignKey(
        User,
        verbose_name='author',
        help_text='Автор',
        on_delete=models.CASCADE,
        related_name='subscribed'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'),
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} => {self.author}'


class IsFavorited(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Любитель',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        help_text='Рецепт',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorited')
        ]
        verbose_name = 'Любимый'
        verbose_name_plural = 'Любимые '

    def __str__(self):
        return f'{self.user} => {self.recipe}'


class IsInShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Покупатель',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        help_text='Рецепт',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping'
            )
        ]
        verbose_name = 'В корзине'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user} => {self.recipe}'
