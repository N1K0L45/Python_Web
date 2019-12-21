from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from elementos.models import *
from .forms import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        if("username" in request.POST.keys()) and ("password" in request.POST.keys()):
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                contexto={"okey":"okey"}
                return redirect("/home/",contexto)
            else:
                contexto={"error":"error"}
                return render(request, 'login.html', contexto)
        else:
            contexto={"error":"error"}
            return render(request, "login.html", contexto)
    return render(request,'login.html')

@login_required(login_url='/login')
def vista_log(request):
    contexto={"okey":"okey"}
    if request.method == 'POST':
        if("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect('/login')
    return render(request,'home.html',contexto)

@login_required(login_url='/login')
def todo(request):
    pelis = Pelicula.objects.all()
    form = tablaForm(request.POST or None)
    if request.method == 'POST':
        if("filtro" in request.POST.keys()):
            filtro = request.POST['filtro']
            if("f2" in request.POST.keys()):
                f2 = request.POST['f2']
                if(filtro=='0'):
                    pelis = Pelicula.objects.all()
                elif(filtro=='titulo'):
                    pelis = Pelicula.objects.filter(titulo__icontains=f2)
                elif(filtro=='tituloAlt'):
                    pelis = Pelicula.objects.filter(tituloAlt__icontains=f2)
                elif(filtro=="anno"):
                    pelis = Pelicula.objects.filter(anno__contains=f2)
                elif(filtro=="director"):
                    pelis = Pelicula.objects.filter(director__nombre__icontains=f2)
                elif(filtro=="actor"):
                    pelis = Pelicula.objects.filter(actor__nombre__icontains=f2)
                elif(filtro=="genero"):
                    pelis = Pelicula.objects.filter(genero__icontains=f2)

    contexto={"okey":"okey", "pelis":pelis, "form":form}
    return render(request,'todo.html',contexto)

@login_required(login_url='/login')
def nuevoItem(request):
    contexto = {"okey":"okey"}
    if request.method == 'POST':
        if("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect('/login')
        form = nuevoForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = nuevoForm(request.POST or None)
    contexto = {"okey":"okey", "form":form}
    return render(request,'nuevo.html',contexto)

@login_required(login_url='/login')
def nuevoDirector(request):
    contexto = {"okey":"okey"}
    if request.method == 'POST':
        if("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect('/login')
        form = nuevoDirectorForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = nuevoDirectorForm(request.POST or None)
    contexto = {"okey":"okey", "form":form}
    return render(request,'nuevoDirector.html',contexto)

@login_required(login_url='/login')
def nuevoActor(request):
    contexto = {"okey":"okey"}
    if request.method == 'POST':
        if("cerrar" in request.POST.keys()):
            auth.logout(request)
            return redirect('/login')
        form = nuevoActorForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = nuevoActorForm(request.POST or None)
    contexto = {"okey":"okey", "form":form}
    return render(request,'nuevoActor.html',contexto)

@login_required(login_url='/login')
def Actores(request):
    actors = Actor.objects.all()
    form = actorForm(request.POST or None)
    if request.method == 'POST':
        if("filtro" in request.POST.keys()):
            filtro = request.POST['filtro']
            if("f2" in request.POST.keys()):
                f2 = request.POST['f2']
                if(filtro=='0'):
                    actors = Actor.objects.all()
                elif(filtro=='nombre'):
                    actors = Actor.objects.filter(nombre__icontains=f2)
                elif(filtro=='birth'):
                    actors = Actor.objects.filter(birth__icontains=f2)
                elif(filtro=="nacion"):
                    actors = Actor.objects.filter(nacion__contains=f2)

    contexto={"okey":"okey", "actors":actors, "form":form}
    return render(request,'actores.html',contexto)

@login_required(login_url='/login')
def Directores(request):
    directors = Director.objects.all()
    form = directorForm(request.POST or None)
    if request.method == 'POST':
        if("filtro" in request.POST.keys()):
            filtro = request.POST['filtro']
            if("f2" in request.POST.keys()):
                f2 = request.POST['f2']
                if(filtro=='0'):
                    directors = Director.objects.all()
                elif(filtro=='nombre'):
                    directors = Director.objects.filter(nombre__icontains=f2)
                elif(filtro=='birth'):
                    directors = Director.objects.filter(birth__icontains=f2)
                elif(filtro=="nacion"):
                    directors = Director.objects.filter(nacion__contains=f2)

    contexto={"okey":"okey", "directors":directors, "form":form}
    return render(request,'directores.html',contexto)
