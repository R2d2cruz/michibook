from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Maullido(models.Model):
    postUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maullidos")
    body = models.CharField(max_length=151)
    postDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.postUser.username + " - " + self.body
    
    class Meta:
        ordering = ['-postDate'] 

    @property
    def happys_count(self):
        return self.reactions.filter(reaction='happy').count()

    @property
    def sads_count(self):
        return self.reactions.filter(reaction='sad').count()

    @property
    def loves_count(self):
        return self.reactions.filter(reaction='love').count()

    @property
    def shockeds_count(self):
        return self.reactions.filter(reaction='shocked').count()

    @property
    def angrys_count(self):
        return self.reactions.filter(reaction='angry').count()


class MaullidoReaction(models.Model):
    REACTION_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('love', 'Love'),
        ('shocked', 'Shocked'),
        ('angry', 'Angry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maullido = models.ForeignKey(Maullido, on_delete=models.CASCADE, related_name="reactions")
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'maullido')

    def __str__(self):
        return f"{self.user.username} → {self.maullido.id} ({self.reaction})"

