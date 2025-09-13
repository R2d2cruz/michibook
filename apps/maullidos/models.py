from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Maullido(models.Model):
    postUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maullidos")
    body = models.CharField(max_length=151)
    postDate = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return self.postUser.username + " - " + self.body