from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        user=User.objects.create_user(username=username, email=email, password=password1, pas)

    return render(request, 'register.html', {})