from django.shortcuts import render
from django.http import HttpResponse

from apps.contato.models import Contato

def index(requisicao):

    dados = {
        1: {
            "nome": "Chico",
            "fone": "9999-8888"
        },
        2: {
            "nome": "Zé",
            "fone": "7777-5555"
        }
    }

    dados = Contato.objects.all()

    return render(requisicao, 'home.html', {"contatos": dados})
