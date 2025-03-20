from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ProyectoUsuarioRol, Proyecto, Tarea
from datetime import datetime, timedelta


def ver_proyectos(request):

    # Obtener el usuario logueado
    usuario_logueado = request.user
    
    # Filtrar los id_proyecto donde id_user sea el usuario logueado y estado sea True
    proyectos = ProyectoUsuarioRol.objects.filter(id_user=usuario_logueado, estado=True).values_list('id_proyecto', flat=True)
    
    # Convertir queryset en lista de ids de proyectos
    id_proyectos = list(proyectos)
    
    # Buscar los proyectos cuyo id_proyecto esté en la lista de id_proyectos
    proyectos_titulos = Proyecto.objects.filter(id_proyecto__in=id_proyectos, estado=True).values('id_proyecto', 'titulo')
    
    context = {'proyectos': proyectos_titulos}
    return render(request, 'proyectos.html', context)

def login_usuario(request):
    if request.method=='POST':
        usuario=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=usuario,password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error (request, "Usuario o contraseña incorrecta")
            return redirect('login')
    return render(request,"login.html",{})

def principal(request): 
    saludo = "Bienvenido %s" %(request.user)
    nombre = "Linea de tiempo"
    context ={
        "nombre": nombre,
        "saludo": saludo,
    }
    return render(request,"principal.html",context)

def inicio(request): 
    return render(request,"base.html")


def cerrar(request):
    logout(request)
    return redirect('login')

def detalle_proyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(pk=id_proyecto)
    tareas = Tarea.objects.filter(id_proyecto=proyecto)

    # Lista de días del año
    days_in_year = list(range(1, 366))  # para 365 días (ajustar a 366 si es bisiesto)

    # Calcula la posición y duración de cada tarea
    for tarea in tareas:
        start_date = tarea.fecha_inicio_estimada
        end_date = tarea.fecha_fin_estimada

        # Calcula el número total de días en el año
        start_datetime = datetime(start_date.year, start_date.month, start_date.day)
        end_datetime = datetime(end_date.year, end_date.month, end_date.day)

        # Total de días en el año
        total_days = (datetime(start_date.year, 12, 31) - datetime(start_date.year, 1, 1)).days + 1
        start_position = ((start_datetime - datetime(start_date.year, 1, 1)).days / total_days) * 100
        duration = ((end_datetime - start_datetime).days / total_days) * 100

        tarea.start_position = start_position
        tarea.duration = duration

    context = {
        'proyecto': proyecto,
        'tareas': tareas,
        'days_in_year': days_in_year,
    }
    return render(request, 'detalle_proyecto.html', context)