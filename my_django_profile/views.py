from django.shortcuts import render

def home(request):
    return render(request, 'my_django_profile/home.html', {"name": "Luis"})

