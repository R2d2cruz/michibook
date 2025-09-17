from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from datetime import datetime

from apps.users.models import UserProfile

# Create your views here.
def signIn(request):
    if request.method == 'GET':
        return render(request, 'signIn.html')
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signIn.html', {
                'error': "Usuario o contraseña equivocados",
            })
        login(request, user)
        return redirect("feed")
        


def signUp(request):
    if request.method == 'GET':
        return render(request, 'signUp.html', {
            'form': UserCreationForm,
        })
    elif request.method == 'POST':
        error = ""
        print(request.POST)
        if request.POST["password"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"], 
                                                first_name=request.POST["first_name"], last_name=request.POST["last_name"], 
                                                email=request.POST["email"])
                user.save()
                login(request, user)
                birthDateStr = request.POST['birthDate']
                try:
                    birthDate = datetime.strptime(birthDateStr, "%d/%m/%Y").date()
                except ValueError:
                    birthDate = None

                profile = UserProfile(user=user, birthDate=birthDate)
                profile.save()
                
                return redirect("userEditProfile", user.username)
            except IntegrityError:
                error = "Usuario ya existe"
        else:
            error = "Las contraselas no son iguales"
        return render(request, 'signUp.html', {
            'form': UserCreationForm,
            'error': error,
        })

@login_required 
def signOut(request):
    user = request.user
    logout(request)
    return redirect("feed")