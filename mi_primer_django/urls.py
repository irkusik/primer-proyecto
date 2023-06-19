"""
URL configuration for mi_primer_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from mi_primer_django.views import inicio, segunda_vista, fecha_actual
from mi_primer_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', inicio),
    path('', views.inicio),
    #path('segunda-vista/', segunda_vista),
    path('segunda-vista/', views.segunda_vista),
    #path('fecha-actual/', fecha_actual)
    path('fecha-actual/',views.fecha_actual),
    path('saludar/',views.saludar),
    path('saludar/<str:nombre>/<str:apellido>/',views.bienvenida)
]
