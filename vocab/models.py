from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    english = models.CharField(max_length=100, unique=True)
    meaning = models.CharField(max_length=255)
    example_sentence = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

def _str_(self):
    return self.english

class LearningProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='not_learned')
    last_reviewed = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'word')
    
    def _str_(self):
        
        return f"{self.user.username} - {self.word.english} ({self.status})"