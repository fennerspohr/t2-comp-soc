"""bdedica URL Configuration

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
from django.urls import path
from bdedicaapp.views import MSEAPIView, AdolescenteAPIView, AtoInfracionalAPIView, MSEFilterView, MSEUpdateView, AdolescenteFiltroView, AdolescenteUpdateView

urlpatterns = [
    path('admin/', admin.site.urls), #site de adm do django
    path('api/atoinfracional/', AtoInfracionalAPIView.as_view()), #url pra dar get nos atos infracionais
    path('api/mse/', MSEAPIView.as_view()), #url pra dar get na lista completa de mse, pegar 1 mse e também post no cadastro
    path('api/mse/filtro', MSEFilterView.as_view()), #url pra dar get nas listas filtradas
    path('api/mse/update', MSEUpdateView.as_view()), #url pra fazer update dos mse
    path('api/adolescente/', AdolescenteAPIView.as_view()), #url pra dar get na lista completa de adolescentes, pegar 1 adolescente e também post no cadastro
    path('api/adolescente/filtro', AdolescenteFiltroView.as_view()), #url pra dar get nas listas filtradas
    path('api/adolescente/update', AdolescenteUpdateView.as_view()), #url pra fazer update dos adolescentes
] 
