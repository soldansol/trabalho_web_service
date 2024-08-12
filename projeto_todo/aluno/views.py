from django.shortcuts import render

# Create your views here.
# aluno/views.py
from django.http import HttpResponse

def atividade_realizada(request):
    return HttpResponse("Realizado com sucesso a atividade")
