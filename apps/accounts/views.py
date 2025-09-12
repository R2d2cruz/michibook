from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
        


def singup(request):
    return render(request, 'singup.html')