from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from apps.maullidos.models import Maullido
from django.contrib.auth.decorators import login_required
from .models import UserProfile


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
    

@login_required
def userEditProfile(request, username):
    try:
        user = get_object_or_404(User, username=username)
        userProfile = get_object_or_404(UserProfile, user=user)
        print(userProfile.birthDate)
    except User.DoesNotExist:
        return render(request, 'userProfile.html', {
            'error': "Usuario " + username + " no encontrado"
        })
    if request.method == "POST":
        userServer = request.user
        if username == userServer.username:
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            userProfile.biography = request.POST['biography']
            userProfile.birthDate = request.POST['birthDate']
            userProfile.save()
            return redirect('userProfile', username)
    return render(request, 'userEditProfile.html', {
        "user": user,
        "profile": userProfile
    })