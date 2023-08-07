from django.shortcuts import render
from .models import Calculo

def home(request):
    return render(request,'peso_altura/home.html')

def calcular(request):
    # Realizar o cálculo 
    num1 = float (request.POST.get('peso'))
    num2 = float (request.POST.get('altura'))
    resultado = num1 / (num2 ** 2)
    

  
    # Passar o resultado 
    return render(request, 'peso_altura/home.html', {'resultado': resultado})



