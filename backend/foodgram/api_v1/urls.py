import path as path
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet, TagViewSet, FollowViewSet, FavoriteVeiwSet, ShoppingcartViewSet, UserListViewSet

v1_router = DefaultRouter()
v1_router.register('users', UserListViewSet,basename='users')
v1_router.register('recipes', RecipeViewSet, basename='recipes')
v1_router.register('recipe/<int:recipe_id/', RecipeViewSet, basename='recipes')
v1_router.register('recipe/<int:recipe_id>/favorite/', FavoriteVeiwSet)
v1_router.register('recipe/<int:recipe_id>/shopping_cart/', ShoppingcartViewSet)
v1_router.register('ingredients', IngredientViewSet, basename='ingredients')
v1_router.register('ingredients/<int:ingredient_id>/', IngredientViewSet, basename='ingredient')
v1_router.register('tags', TagViewSet, basename='tags')
v1_router.register('tags/<int:tag_id', TagViewSet, basename='tags')
v1_router.register('subscription', FollowViewSet, basename='subscription')

# v1_router.register('recipe/<int:recipe_id/favorite/', FavoriteVeiwSet)
# v1_router.register('recipe/<int:recipe_id>/shoppingcart/', ShoppingcartViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
]