from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Victor'})

def add(request):

    valor1 = int(request.POST['num1'])
    valor2 = int(request.POST['num2'])

    res = valor1 + valor2

    return render(request, "result.html", {'resultado':res})