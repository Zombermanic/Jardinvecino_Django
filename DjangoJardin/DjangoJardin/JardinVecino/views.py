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

def usuarionuevo(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        appPaterno = request.POST.get("appPaterno")
        appMaterno = request.POST.get("appMaterno")
        correo = request.POST.get("correo")
        
        
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            correo=correo,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        
        return render(request, "usuarionuevo.html", context)
    else:
        return render(request, "usuarionuevo.html")