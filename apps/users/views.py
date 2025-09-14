from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from apps.maullidos.models import Maullido


# Create your views here.
def userProfile(request, username):
    try:
        userProfile = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        return render(request, 'userProfile.html', {
            'error': "Usuario " + username + " no encontrado"
        })
    if request.method == "POST":
        user = request.user
        if username == user.username:
            maullido = Maullido.objects.create(postUser= user ,body= request.POST['maullido'])
            maullido.save()
            return redirect('userProfile', username)
    posts = userProfile.maullidos.all()
    return render(request, 'userProfile.html', {
        'userProfile': userProfile,
        'posts': posts,
    })


def users(request):
    users = User.objects.all
    return render(request, 'users.html', {
        'users': users,
    })