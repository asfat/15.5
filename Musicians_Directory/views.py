from django.shortcuts import render
from album.models import Album

def home(request):
    album=Album.objects.all()
    print(album)
    for i in album:
        print(i.rating)
        
            
        
    return render(request,'home.html',{'album':album})