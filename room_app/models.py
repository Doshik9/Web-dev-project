from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
        help_text='Название комнаты',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата создания комнаты',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Дата обновления комнаты',
    )