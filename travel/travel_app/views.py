from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name='Brasov'
    dest1.desc='Brasov is the best'
    dest1.price=300
    dest1.img='destination_1.jpg'
    dest1.offer=False

    dest2=Destination()
    dest2.name='Sinaia'
    dest2.desc='Sinaia rocks!!!'
    dest2.price=150
    dest2.img='destination_2.jpg'
    dest2.offer=True

    dest3=Destination()
    dest3.name='Sibiu'
    dest3.desc='I love Sibiu!'
    dest3.price=450
    dest3.img='destination_3.jpg'
    dest3.offer=False

    destinations=[dest1, dest2, dest3]
    return render(request, 'index.html', {'price':700, 'destinations':destinations})