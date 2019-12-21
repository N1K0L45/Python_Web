from django.shortcuts import render

# Create your views here.

def idem(request):
    return render(request, 'idem.html')
