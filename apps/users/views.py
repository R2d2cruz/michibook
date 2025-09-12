from django.shortcuts import render

# Create your views here.
def userProfile(request, user_name):
    return render(request, 'userProfile.html')


def users(request):
    return render(request, 'users.html')