from django.shortcuts import render

# Create your views here.
def singin(request):
    return render(request, 'singin.html')


def singup(request):
    return render(request, 'singup.html')