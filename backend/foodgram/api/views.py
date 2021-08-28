from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    TagSerializer,
    SubscribeSerializer,
    FavoriteSerializer,
    ShoppingSerializer,
    UserSerializer,
    ListRecipeSerializer,
    CreateRecipeSerializer,

)
from api.models import Recipe, Ingredient, Tag, Subscribe
from users.models import CustomUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .paginators import PageNumberPaginatorModified
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from .permissions import AdminOrAuthorOrReadOnly




class UserListViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPaginatorModified
    queryset = CustomUser.objects.all()
    http_method_names = ('get', 'post')
    filter_backends = [DjangoFilterBackend]
    filteset_fields = ['email', 'username']


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    # permission_classes = (AdminOrAuthorOrReadOnly,)
    permission_classes = [AllowAny]
    pagination_class = PageNumberPaginatorModified
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'name', 'tags']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ListRecipeSerializer
        return CreateRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context



class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    pagination_class = None
    queryset = Ingredient.objects.all()

    # def list(self, request):
    #     queryset = Ingredient.objects.all()
    #     serializer = IngredientSerializer(queryset, many=True)
    #     return Response(serializer.data)

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


class SubscribeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    http_method_names = ('get', 'post')
    queryset = Subscribe.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.subscribed.all()
