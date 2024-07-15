from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


class signin(View):
    def get(self, request):
        return render(request, 'Authentication/sign_in.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'Authentication/sign_up.html', {'form': form})
   
    
class lockscreen(View):
    def get(self, request):
        return render(request, 'Authentication/lockscreen.html')

class logout(View):
    def get(self, request):
        return render(request, 'Authentication/logout.html')

class sucess(View):
    def get(self, request):
        return render(request, 'Authentication/sucess.html')
    