from django.shortcuts import render

def index(request):
    return render(request, 'Expenses/index.html')

def landing(request):
    return render(request, 'Landing/landing.html')

def about(request):
    return render(request, 'Landing/about_us.html')

def helpdesk(request):
    return render(request, 'Landing/help_desk.html')

def landingfaq(request):
    return render(request, 'Landing/landing_faq.html')

