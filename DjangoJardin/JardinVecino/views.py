from django.shortcuts import render
from .models import Usuario

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def sobrenosotros(request):

    return render(request, "sobrenosotros.html")

def catalogo(request):

    return render(request, "catalogo.html")

def historial(request):

    return render(request, "historial.html")

def sub(request):

    return render(request, "sub.html")
def admin(request):

    return render(request, "admin.html")

def menu_sesion(request):

    return render(request, "menu_sesion.html")

def seguimiento(request):

    return render(request, "seguimiento.html")

def sesionSocio(request):

    return render(request, "sesionSocio.html")

def pedidos(request):

    return render(request, "pedidos.html")

def PagAdmin(request):

    return render(request, "PagAdmin.html")

def sesion(request):

    return render(request, "sesion.html")

def socio(request):

    return render(request, "socio.html")