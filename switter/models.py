from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        blank=True,
        symmetrical=False
    )

    def __str__(self):
        return str(self.user)
