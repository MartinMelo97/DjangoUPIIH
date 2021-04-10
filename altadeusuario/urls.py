"""gestoralmacen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import AltaUsuarioList, AltaUsuarioDetail, AgregarAltaUsuario, ModificarAltaUsuario, EliminarAltaUsuario

app_name = "altadeusuario"

urlpatterns = [
    path('', AltaUsuarioList.as_view()),
    path('<int:id>', AltaUsuarioDetail.as_view()),
    path('add/', AgregarAltaUsuario.as_view()),
    path('edit/<int:id>', ModificarAltaUsuario.as_view()),
    path('delete/<int:id>', EliminarAltaUsuario.as_view())
]