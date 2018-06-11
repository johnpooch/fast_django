from django.shortcuts import render
from .models import Album

# Create your views here.

def get_index(request):
    
    albums = Album.objects.all()
    
    return render(request, "home/index.html", {"albums": albums})