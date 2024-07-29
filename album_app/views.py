from django.shortcuts import render,redirect
from album_app import models
from album_app.forms import album_form
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from album_app.forms import registerModel
from django.contrib.auth import login,logout

from django.contrib.auth.decorators import login_required
# Create your views here.

def album(request):
    data = models.Album.objects.all()
    print(data)
    return render(request,'home.html',{'data':data})


@login_required
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

@login_required
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
def registerform(request):
    if request.method == 'POST':
        form = registerModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = registerModel()
    return render(request,'register.html',{'form':form})



class register(CreateView):
    model = User
    form_class = registerModel
    template_name = 'register.html'
    success_url = reverse_lazy('log_in')
    
    
# class log_in(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'register.html'
    
#     # success_url = reverse_lazy('album_app')
    
#     def get_success_url(self):
#         return reverse_lazy('album_app')
    
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request.user,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            user = authenticate(username =user_name,password = pass_word)
            if user is not None:
                login(request,user)
                return redirect('album_page')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('log_in')