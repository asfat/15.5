from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def musician(request):
    if request.method=='POST':
        form=forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('musician')
    else:
        form=forms.MusicianForm()
    return render(request,'musician.html',{'form':form})

def musician_edit(request,id):
    editMusician=models.Musician.objects.get(pk=id)
    editpost=forms.MusicianForm(instance=editMusician)
    if request.method=='POST':
        editpost=forms.MusicianForm(request.post,instance=editpost)
        if editpost.is_valid():
            editpost.save()

        return redirect('home')
    return render(request,'album.html',{'form':editpost})
