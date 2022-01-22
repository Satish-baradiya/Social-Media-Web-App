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

class Sweet(models.Model):
    user = models.ForeignKey(
        User, related_name="sweets", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M}):"
            f"{self.body[:30]}..."
        )
