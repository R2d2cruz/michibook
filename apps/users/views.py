from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.
def userProfile(request, username):
    try:
        user = get_object_or_404(User, username=username)
        posts = user.maullidos.all()
        return render(request, 'userProfile.html', {
            'user': user,
            'posts': posts,
        })
    except User.DoesNotExist:
        return render(request, 'userProfile.html', {
            'error': "Usuario " + username + " no encontrado"
        })


def users(request):
    users = User.objects.all
    return render(request, 'users.html', {
        'users': users,
    })