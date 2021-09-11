from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    FavoriteVeiwSet,
    SubscribeViewSet,
    IngredientViewSet,
    RecipeViewSet,
    ShoppingcartViewSet,
    TagViewSet,
    UserListViewSet
)

v1_router = DefaultRouter()
v1_router.register('recipes', RecipeViewSet, basename='recipes')
v1_router.register(
    'recipe/<int:recipe_id/',
    RecipeViewSet,
    basename='recipes'
)
v1_router.register(
    'recipe/<int:recipe_id>/favorite/',
    FavoriteVeiwSet,
    basename='favorite'
)
v1_router.register(
    'recipe/<int:recipe_id>/shopping_cart/',
    ShoppingcartViewSet,
    basename='shopping_cart'
)
v1_router.register(
    'ingredients',
    IngredientViewSet,
    basename='ingredients'
)
v1_router.register(
    'ingredients/<int:ingredient_id>/',
    IngredientViewSet,
    basename='ingredient'
)
v1_router.register('tags', TagViewSet, basename='tags')
v1_router.register('tags/<int:tag_id', TagViewSet, basename='tags')
v1_router.register(
    'subscription',
    SubscribeViewSet,
    basename='subscription'
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

]
