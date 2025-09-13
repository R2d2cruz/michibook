from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.
def userProfile(request, username):
    try:
        user = get_object_or_404(User, username=username)
        return render(request, 'userProfile.html', {
            'user': user
        })
    except:
        return render(request, 'userProfile.html', {
            'error': "Usuario " + username + " no encontrado"
        })


def users(request):
    return render(request, 'users.html')