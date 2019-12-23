from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Position(models.Model):
    post = models.CharField(max_length=600)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.post
    
    def get_absolute_url(self):
        return "/vote/{}".format(self.slug)
    
    def user_can_vote(self, user):
        # Returns false if user has already voted.
        user_votes = user.vote_set.all()
        qs = user_votes.filter(post=self)

        if qs.exists():
            return False
        return True

    
    
class Aspirant(models.Model):
    name = models.CharField(max_length=600)
    post = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def num_votes(self, aspirant):
        qs = self.vote_set.get(aspirant=aspirant)
        return qs.count()


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE, null=True)

