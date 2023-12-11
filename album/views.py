from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def album(request):
    if request.method=='POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('album')
    else:
        form=forms.AlbumForm()
    return render(request,'album.html',{'form':form})

def album_edit(request, id):
    edit_album = models.Album.objects.get(pk=id)
    post_album = forms.AlbumForm(instance=edit_album)

    if request.method == 'POST':
        post_album = forms.AlbumForm(request.POST, instance=edit_album)
        if post_album.is_valid():
            post_album.save()
            return redirect('home')

    return render(request, 'album.html', {'form': post_album})

def delete_add(request,id):
    edit_album=models.Album.objects.get(pk=id)
    edit_album.delete()
    return redirect('home')

    
        