from django.shortcuts import render
from .models import Usuario

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")