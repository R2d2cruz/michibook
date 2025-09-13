from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    biography = models.TextField(null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Perfil de usuario " + self.user.username