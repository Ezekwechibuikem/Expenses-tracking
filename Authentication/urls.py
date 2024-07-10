from django.urls import path
from .views import signin, signup, lockscreen, logout, success

urlpatterns = [
    path('signin/', signin.as_view(), name='signin'),
    path('signup/', signup.as_view(), name='signup'),
    path('lockscreen/', lockscreen.as_view(), name='lockscreen'),
    path('logout/', logout.as_view(), name='logout'),
    path('success/', success.as_view(), name='success'),
]
