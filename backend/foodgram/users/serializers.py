from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import CustomUser
from api_v1.models import Follow


class CustomUserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            'id', 'email', 'username', 'password', 'first_name', 'last_name'
        )


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()
    """Serializer пользователя"""

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed',)

        def get_is_subscribed(self, obj):
            request = self.context.get('request')
            if request is None or request.user.is_anonymous:
                return False
            return Follow.objects.filter(user=request.user, author=obj).exists()

    # class AuthSerializer(serializers.Serializer):
    #     """Serializer аутентификации"""
    #     email = serializers.EmailField(required=True)
    #     confirmation_code = serializers.CharField(required=True)

# class ConfirmationSerializer(serializers.Serializer):
#     """Serialize отправки кода кодтверждения и регистраци"""
#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
