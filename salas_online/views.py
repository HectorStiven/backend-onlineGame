from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def control(request):
    return render(request, "control.html")



def pantalla(request):
    return render(request, "pantalla.html")