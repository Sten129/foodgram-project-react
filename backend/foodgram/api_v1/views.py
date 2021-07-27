from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    TagSerializer,
    FollowSerializer,
    FavoriteSerializer,
    ShoppingSerializer)
from api_v1.models import Recipe, Ingredient, Tag, Follow
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAuthorOrReadOnly

PERMISSION_CLASSES = [IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthorOrReadOnly]


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'name', 'tag']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    pass


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    queryset = Ingredient.objects.all()

    pass


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    queryset = Tag.objects.all()
    pass


class FavoriteVeiwSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Recipe.objects.all()

    class Meta:
        fields = '__all__'

    pass


class ShoppingcartViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingSerializer
    queryset = Recipe.objects.all()

    class Meta:
        fields = '__all__'

    pass


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    http_method_names = ('get', 'post')
    # search_fields = ['user__username, 'following__username']
    queryset = Follow.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.following.all()

    pass
