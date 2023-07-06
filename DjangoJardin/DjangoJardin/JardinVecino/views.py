import requests
import json
from django.shortcuts import render
from .models import Usuario, tipoUsuario
from .forms import UsuarioForm, tipoForm

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

#lo que si tiene codigo de mas aqui
def borrar_usuario(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...", "usuario": usuarios}
        return render(request, "lista_usuarios.html", context)

def userUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.rut = rut
        user.nombre = nombre
        user.appPaterno = appPaterno
        user.appMaterno = appMaterno
        user.fechaNacimiento = fecha
        user.tipoUsuario = objTipo
        user.correo = correo
        user.telefono = telefono
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "OK Registro modificado", "tipo": tipo, "usuario": user}

        return render(request, "pages/user_edit.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "pages/user_list.html", context)

def editar_usuario(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "lista_usuarios.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "lista_usuarios", context)

def crudTipo(request):
    tipos = tipoUsuario.objects.all()
    context = {"tipo": tipos}
    return render(request, "pages/tipo_list.html", context)

def tipoAdd(request):
    if request.method != "POST":
        tipo = tipoForm()
        context = {"tipo": tipo}
        return render(request, "agragar_tipo.html", context)
    else:
        form = tipoForm(request.POST)
        if form.is_valid():
            form.save()

            form = tipoForm()

            context = {"mensaje": "OK Agregado con exito", "tipo": form}
            return render(request, "agragar_tipo.html", context)


def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "lista_usuarios.html", context)      

def usuarionuevo(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "usuarionuevo.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        #region_id = request.POST.get('cboRegiones')
        #comuna_id = request.POST.get('cboComunas')

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        # Guardar el usuario en la base de datos
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            tipoUsuario=objTipo,
            correo=correo
        )

        # Obtener el nombre de la región utilizando requests
        #region_data = requests.get(f"https://apis.digital.gob.cl/dpa/regiones/{region_id}").json()
        ##region = region_data['nombre']

        # Obtener el nombre de la comuna utilizando requests
        #comuna_data = requests.get(f"https://apis.digital.gob.cl/dpa/comunas/{comuna_id}").json()
        #comuna = comuna_data['nombre']

        # Asignar la región y comuna al usuario y guardar los cambios
        #objUsuario.region = region
       #objUsuario.comuna = comuna
        #objUsuario.save()

        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "usuarionuevo.html", context)