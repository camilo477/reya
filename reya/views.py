from django.contrib.auth.views import LoginView  # Importa la vista de inicio de sesión predeterminada
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User  # Importa el modelo de usuario
from django.shortcuts import render, redirect
from django.contrib import messages 

# Define la vista personalizada de inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'pages/elegir.html'  # Establece la plantilla adecuada

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar si el usuario existe
        user = authenticate(username=username, password=password)
        if user is not None:
            # El usuario existe, iniciar sesión
            login(request, user)
            return redirect('elegir')  # Redirige al usuario a la vista 'elegir' después de iniciar sesión
        else:
            # El usuario no existe, muestra un mensaje de error y redirige a la página principal
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('principal')  # Redirige al usuario a la vista 'principal'

# Las otras vistas siguen igual
def guardar_usuario(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        user, created = User.objects.get_or_create(username=correo, email=correo)
        if created:
            user.set_password(contraseña)
            user.save()
            user = authenticate(username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('principal')  # Redirige al usuario a la vista 'elegir' después de iniciar sesión
    return render(request, 'pages/crearUsuario.html')

def principal(request):
    return render(request, 'pages/index.html')

def elegir(request):
    return render(request, 'pages/elegir.html')

def crear(request):
    return render(request, 'pages/crearUsuario.html')

def comida1(request):
    return render(request, 'pages/comida-1.html')

def comida2(request):
    return render(request, 'pages/comida-2.html')

def comida3(request):
    return render(request, 'pages/comida-3.html')

def perfil(request):
    return render(request, 'pages/perfil.html')