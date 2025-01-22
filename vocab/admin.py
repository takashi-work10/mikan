from django.contrib import admin
from .models import Word, LearningProgress

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('english', 'meaning', 'created_at')
    
@admin.register(LearningProgress)
class LearningProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'status', 'last_reviewed')


