from django.urls import path
from .views import *
app_name = "base"
urlpatterns = [
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
]