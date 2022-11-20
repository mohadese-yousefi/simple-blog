from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=225)

    def __str__(self):
        return self.title
    
    

class Score(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postscore')
    score_number = models.SmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user} {self.post.title}'