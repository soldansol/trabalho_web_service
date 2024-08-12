
from django.urls import path
from .views import atividade_realizada

urlpatterns = [
    path('aluno/', atividade_realizada),
]
