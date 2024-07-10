from django.shortcuts import render
from django.views import View

class signin(View):
    def get(self, request):
        return render(request, 'Authentication/sign_in.html')

class signup(View):
    def get(self, request):
        return render(request, 'Authentication/sign_up.html')
    
class lockscreen(View):
    def get(self, request):
        return render(request, 'Authentication/lockscreen.html')

class logout(View):
    def get(self, request):
        return render(request, 'Authentication/logout.html')

class sucess(View):
    def get(self, request):
        return render(request, 'Authentication/sucess.html')
    