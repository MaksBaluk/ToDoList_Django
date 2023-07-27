from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTemplate.as_view(), name='main'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
]
