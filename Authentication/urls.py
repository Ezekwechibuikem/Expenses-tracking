from django.urls import path
from .views import signin, lockscreen, logout, sucess
from .views import register
from . import views

urlpatterns = [
    path('signin/', signin.as_view(), name='signin'),
    path('signup/', register, name='signup'),
    path('lockscreen/', lockscreen.as_view(), name='lockscreen'),
    path('logout/', logout.as_view(), name='logout'),
    path('success/', sucess.as_view(), name='success'),
    path('test-db/', views.test_db, name='test_db'),
]
