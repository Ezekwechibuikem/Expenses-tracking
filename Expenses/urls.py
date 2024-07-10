from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.landing, name='landing'),
    path('about_us/', views.about, name='about'),
    path('help_desk/', views.helpdesk, name='helpdesk'),
    path('landing_faq/', views.landingfaq, name='landing_faq'),
    
]