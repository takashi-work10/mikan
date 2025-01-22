from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Word, LearningProgress

def home(request):
    return render(request, 'vocab/home.html')

@login_required
def learn(request):
    not_learned = Word.objects.exclude(
        learningprogress__user=request.user
    ).first()

    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        action = request.POST.get('action')
        word = Word.objects.get(id=word_id)
        lp, created = LearningProgress.objects.get_or_create(
        user=request.user,
        word=word,
        defaults={'status': 'learning'}
        )
        if action == 'known':
            lp.status = 'learned'
        elif action == 'unknown':
            lp.status = 'learning'
        lp.save()
        return redirect('vocab:learn')

    context = {
        'word': not_learned,
    }
    return render(request, 'vocab/learn.html', context)

@login_required
def my_progress(request):
    lp_list= LearningProgress.objects.filter(user=request.user)
    return render(request, 'vocab/my_progress.html', {'lp_list': lp_list})



