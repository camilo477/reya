from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('crear/', views.crear, name='crear'),
    path('comida1/', views.comida1, name='comida1'),
    path('comida2/', views.comida2, name='comida2'),
    path('comida3/', views.comida3, name='comida3'),
    path('guardar_usuario/', views.guardar_usuario, name='guardar_usuario'),
    path('elegir/', views.elegir, name='elegir'),
    path('perfil/', views.perfil, name='perfil'),
    # Utiliza la vista personalizada de inicio de sesión
    path('login/', CustomLoginView.as_view(), name='login'),
]