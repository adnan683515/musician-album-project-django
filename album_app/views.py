from django.shortcuts import render,redirect
from album_app import models
from album_app.forms import album_form

# Create your views here.
def album(request):
    data = models.Album.objects.all()
    print(data)
    return render(request,'home.html',{'data':data})


def albumform(request):
    
    if request.method == 'POST':
        form = album_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("album_page")
    else:
        form = album_form()
    
    return render(request,'album.html',{'form':form})


def edit_album(request,id):
    
    data = models.Album.objects.get(pk=id)
    print(data)
    form = album_form(instance=data)
    
    
    if request.method == 'POST':
        form = album_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('album_page')
        
    return render(request,'album.html',{"form":form})
    

# def delete_item(request,id):
#     data = models.Album.objects.get(pk=id)
#     data.delete()
#     return redirect('album_page')
    
    