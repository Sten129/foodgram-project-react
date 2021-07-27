# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# class UserRoles(models.TextChoices):
#     """Роли пользователей"""
#     USER = 'user'
#     MODERATOR = 'moderator'
#     ADMIN = 'admin'
#
#
# class CustomUser(AbstractUser):
#     email = models.EmailField(verbose_name='email адрес',
#                               unique=True, max_length=254)
#     # id = models.ForeignKey()
#     username = models.CharField(max_length=150, verbose_name='Уникальный юзернейм', unique=True)
#     # first_name = models.CharField(verbose_name='Имя', max_length=150)
#     # last_name = models.CharField(verbose_name='Фамилия', max_length=150)
#     is_subscribed = models.BooleanField(verbose_name='Подписан ли текущий пользователь на этого')# ?
#     role = models.CharField(verbose_name='Роль пользователя',
#                             max_length=9,
#                             choices=UserRoles.choices,
#                             default=UserRoles.USER)
#
#     class Meta:
#         ordering = ('-id',)
#
#     @property
#     def is_admin(self):
#         return (self.is_staff
#                 or self.role == UserRoles.ADMIN
#                 or self.is_superuser)
#
#     @property
#     def is_moderator(self):
#         return self.role == UserRoles.MODERATOR
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username