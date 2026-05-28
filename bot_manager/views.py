from django.shortcuts import render
from .models import Track

def index(request):
    # Достаем абсолютно все треки, которые ты добавишь через админку
    tracks = Track.objects.all()
    return render(request, 'index.html', {'tracks': tracks})