from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # email = models.EmailField(
    #     verbose_name='Почта',
    #     unique=True,
    #     blank=True,
    # )
    bio = models.CharField(
        verbose_name='Био',
        blank=True,
        max_length=100,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatars/images/',
        blank=True,
        null=True,
    )
