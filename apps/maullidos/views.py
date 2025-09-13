from django.shortcuts import render
from .models import Maullido

# Create your views here.
def feed(request):
    # Obtiene todos los maullidos en orden descendente por fecha
    posts = Maullido.objects.all().order_by('-postDate')
    
    for m in Maullido.objects.all():
        print(m.id, m.postUser, m.postUser.username if m.postUser else None)
    return render(request, 'feed.html', {
        'posts': posts
    })