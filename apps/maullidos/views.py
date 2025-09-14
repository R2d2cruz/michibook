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
        'posts': posts
    })


@login_required
@require_POST
def reactMaullido(request, maullido_id):
    try:
        maullido = get_object_or_404(Maullido, id=maullido_id)
    except Maullido.DoesNotExist:
        return JsonResponse({"error": "Maullido no encontrado"}, status=404)
    action = request.POST.get("action")
    if action == "like":
        maullido.likes += 1
    elif action == "dislike":
        maullido.dislikes += 1
    maullido.save()
    return JsonResponse({
        "likes": maullido.likes,
        "dislikes": maullido.dislikes
    })