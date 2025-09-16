from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Maullido
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def feed(request):
    # Obtiene todos los maullidos en orden descendente por fecha
    posts = Maullido.objects.all().order_by('-postDate')
    
    return render(request, 'feed.html', {
        'posts': posts,
        "global_feed": True,
    })

@login_required
@require_POST
def createMaullido(request):
    if request.method == "POST":
        text = request.POST.get("maullido", "").strip()
        
        maullido = Maullido.objects.create(postUser=request.user, body=text)
        maullido.save()
        
