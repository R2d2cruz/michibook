from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    AVATAR_CHOICES = [
        ("blackCat", "Gato Negro"),
        ("orangeCat", "Gato Naranja"),
        ("whiteCat", "Gato Blanco"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    biography = models.TextField(null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    avatarChoice = models.CharField(max_length=20, choices=AVATAR_CHOICES, default="blackCat")

    def __str__(self):
        return "Perfil de usuario " + self.user.username