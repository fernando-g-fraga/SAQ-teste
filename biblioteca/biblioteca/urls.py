"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from livros.views import LivrosViewset,RetiradaViewset,LeitoresViewset
from rest_framework import routers
from rest_framework.authtoken import views

Routers = routers.DefaultRouter()
Routers.register(r'livros',LivrosViewset,'livros')
Routers.register(r'leitores',LeitoresViewset,'leitores')
Routers.register(r'retiradas',RetiradaViewset,'retiradas')


urlpatterns = [
    path('',include(Routers.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth',views.obtain_auth_token),
]
