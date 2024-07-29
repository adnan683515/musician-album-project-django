from django.shortcuts import render,redirect
from musican_app.forms import Musician_Form
from musican_app import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def form_musician(request):
    if request.method == 'POST':
        form = Musician_Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('form_musician')
    else:
        form = Musician_Form()
    
    return render(request,'musician.html',{'form':form})


@login_required
def delete_item(request,id):
    data = models.musican.objects.get(pk=id)
    print(data)
    data.delete()
    return redirect('album_page')
    
  
@login_required  
def edit(request,id):
    data  = models.musican.objects.get(pk=id)
    form = Musician_Form(instance=data)
    if request.method== 'POST':
        form = Musician_Form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('album_page')
        
    return render(request,'musician.html',{'form':form})

