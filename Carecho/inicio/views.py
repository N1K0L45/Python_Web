from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {'autor':'Carecho', 'appName':'Careccio'}
    return render(request,'inicio.html',context)
