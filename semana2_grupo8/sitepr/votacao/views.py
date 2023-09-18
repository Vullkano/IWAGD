from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Viva DIAM. Esta e a pagina de entrada da app votacao.")