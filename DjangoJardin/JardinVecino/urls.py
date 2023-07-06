from DjangoJardin.urls import path
from . import views

urlpatterns = [
    path("inicio", views.inicio, name="inicio"),
    path("sobrenosotros.html", views.sobrenosotros, name="sobrenosotros"),
    path("catalogo.html", views.catalogo, name="catalogo"),
    path("historial.html", views.historial, name="historial"),
    path("sub.html", views.sub, name="sub"),
    path("admin.html", views.admin, name="admin"),
    path("menu_sesion.html", views.menu_sesion, name="menu_sesion"),
    path("seguimiento.html", views.seguimiento, name="seguimiento"),
    path("sesionSocio.html", views.sesionSocio, name="sesionSocio"),
    path("pedidos.html", views.pedidos, name="pedidos"),
    path("PagAdmin.html", views.PagAdmin, name="PagAdmin"),
    path("sesion.html", views.sesion, name="sesion"),
    path("socio.html", views.socio, name="socio"),
    path("usuarionuevo.html", views.usuarionuevo, name="usuarionuevo"),
    path("crud", views.crud, name="crud"),
    path("crudTipo", views.crudTipo, name="crudTipo"),
    path("borrar_usuario/ <str:pk>", views.borrar_usuario, name="borrar_usuario"),
    path("editar_usuario/ <str:pk>", views.editar_usuario, name="editar_usuario"),
    path("actualizarUsuario", views.actualizarUsuario, name="actualizarUsuario"),
    path("vistaSocio", views.vistaSocio, name="vistaSocio")
    
]