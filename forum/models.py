from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, related_name='question_user', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500)
    tags = TaggableManager()
    
    def __str__(self):
        return self.question
    
    
class Answer(models.Model):
    author = models.ForeignKey(User, related_name='answer_user', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Question, related_name='answer_question', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.author)