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


@login_required
@require_POST
def reactMaullido(request, maullido_id):
    maullido = get_object_or_404(Maullido, id=maullido_id)
    action = request.POST.get("action")

    if action not in dict(MaullidoReaction.REACTION_CHOICES):
        return JsonResponse({"error": "Reacción no válida"}, status=400)

    reaction, created = MaullidoReaction.objects.get_or_create(
        user=request.user,
        maullido=maullido,
        defaults={'reaction': action}
    )

    if not created:
        if reaction.reaction == action:
            reaction.delete()
        else:
            reaction.reaction = action
            reaction.save()

    return JsonResponse({
        "happys": maullido.happys_count,
        "sads": maullido.sads_count,
        "loves": maullido.loves_count,
        "shockeds": maullido.shockeds_count,
        "angrys": maullido.angrys_count,
    })