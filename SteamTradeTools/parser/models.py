from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class Cases(models.Model):
    """Модель кейсов."""
    name = models.CharField(max_length=100,
                            verbose_name='Название кейса',
                            unique=True)
