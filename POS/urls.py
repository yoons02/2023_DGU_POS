"""POS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('base.urls')),
    path('', views.showOrder, name='showOrder'),
    path('createtable/', views.create, name="createtable"),
    path('update/<int:id>', views.update, name="update"),
    path('endtable/<int:id>', views.endtable, name="endtable"),
    path('showresults/', views.showresults, name="showresults"),
    path('updateresult/<int:id>', views.updateresult, name="updateresult"),
    path('deleteresult/<int:id>', views.deleteresult, name="deleteresult"),

]
