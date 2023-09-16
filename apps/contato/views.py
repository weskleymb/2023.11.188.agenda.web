from django.shortcuts import render
from django.http import HttpResponse

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

    return render(requisicao, 'home.html', {"contatos": dados})
