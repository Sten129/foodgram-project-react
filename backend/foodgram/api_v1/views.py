from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    TagSerializer,
    FollowSerializer,
    FavoriteSerializer,
    ShoppingSerializer,
    UserSerializer
)
from api_v1.models import Recipe, Ingredient, Tag, Follow
from users.models import CustomUser
from rest_framework.pagination import PageNumberPagination
from .paginators import PageNumberPaginatorModified
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from .permissions import AdminOrAuthorOrReadOnly


# PERMISSION_CLASSES = [IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthorOrReadOnly]

class UserListViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPaginatorModified
    queryset = CustomUser.objects.all()
    filter_backends = [DjangoFilterBackend]
    filteset_fields = ['email', 'username']


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = (AdminOrAuthorOrReadOnly,)
    pagination_class = PageNumberPaginatorModified
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'name', 'tags']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = Ingredient.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    pagination_class = None
    permission_classes = (AllowAny,)
    queryset = Tag.objects.all()


class FavoriteVeiwSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticated,)

    class Meta:
        fields = '__all__'


class ShoppingcartViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingSerializer
    queryset = Recipe.objects.all()

    class Meta:
        fields = '__all__'


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
