from django.shortcuts import get_object_or_404
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from api_v1.models import Recipe, Ingredient, Tag, Follow


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Recipe


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(many=False, read_only=True, slug_field='id')

    class Meta:
        fields = '__all__'
        model = Ingredient


class IngredientInRecipeSeralizer(serializers.ModelSerializer):
    pass


class TagSerializer(serializers.ModelSerializer):
    id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='id')

    class Meta:
        fields = '__ALL__'
        model = Tag




class FavoriteSerializer(serializers.ModelSerializer):
    recipes = serializers.SlugRelatedField(slug_field='recipes', queryset=Recipe.objects.all())

    class Meta:
        fields = '__all__'
        model = Recipe


class ShoppingSerializer(serializers.ModelSerializer):
    recipes = serializers.SlugRelatedField(slug_field='recipes', queryset=Recipe.objects.all())

    class Meta:
        fields = '__all__'
        model = Recipe


class FollowSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     slug_field='username',
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    # following = serializers.SlugRelatedField(
    #     slug_field='username',
    #     queryset=User.objects.all()
    # )
    #
    # class Meta:
    #     fields = '__all__'
    #     model = Follow
    #     validators = [UniqueTogetherValidator(
    #         queryset=Follow.objects.all(),
    #         fields=['user', 'following']
    #     )]
    #
    # def validate(self, data):
    #     if self.context['request'].user != data.get('following'):
    #         return data
    #     raise serializers.ValidationError("Нельзя подписаться на самого себя")
    pass
