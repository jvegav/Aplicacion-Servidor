from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from servidor.logic.servidor_logic import *


def index(request):
    return render(request, 'index.html')


        
    