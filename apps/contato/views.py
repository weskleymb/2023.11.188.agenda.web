from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.contato.models import Contato
from apps.contato.forms import ContatoForms

def index(requisicao):
    dados = Contato.objects.all()
    return render(requisicao, 'index.html', {"contatos": dados})

def form(requisicao):
    
    form = ContatoForms()

    if requisicao.method == 'POST':
        form = ContatoForms(requisicao.POST)

        if form['nome'].value() != '' and form['fone'].value() != '':
            nome_form = form['nome'].value()
            fone_form = form['fone'].value()
            
            contato = Contato(nome=nome_form, fone=fone_form)
            contato.save()

            return redirect('index')

    return render(requisicao, 'form.html', {"form": form})
