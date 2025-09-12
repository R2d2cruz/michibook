from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

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
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("feed")
            except IntegrityError:
                error = "Usuario ya existe"
        else:
            error = "Las contraselas no son iguales"
        return render(request, 'signUp.html', {
            'form': UserCreationForm,
            'error': error,
        })