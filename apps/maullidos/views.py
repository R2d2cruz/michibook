from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Maullido, MaullidoReaction
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def feed(request):
    # Obtiene todos los maullidos en orden descendente por fecha
    posts = Maullido.objects.all().order_by('-postDate')
    
    return render(request, 'feed.html', {
        'posts': posts
    })
