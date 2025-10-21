#from django.shortcuts import render

# Consultar documentação Django para saber o pacote que contem a classe desejada
from django.views.generic.edit import CreateView, UpdateView

from .models import Campo, Atividade, Campus, Status, Classe

# Recursos para ações com o registro após cadastro criado
from django.urls import reverse_lazy

# Create your views here.

#Criar as classes herdadas de CreateView para criação de cada tipo de cadastro que temos
class CampoCreate(CreateView):
    model = Campo
    # Informar quais campos deseja que sejam preenchidos -- vide disponíveis em models.py
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    # Em caso de preenchimento correto de todos os campos, vai por enquanto para o início (index)
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CampusCreate(CreateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


# Update your views here.

#Editar (UPDATE) as classes herdadas de UpdateView para cada tipo de cadastro que temos
class CampoUpdate(UpdateView):
    model = Campo
    # Informar quais campos deseja que sejam preenchidos -- vide disponíveis em models.py
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    # Em caso de preenchimento correto de todos os campos, vai por enquanto para o início (index)
    success_url = reverse_lazy('index')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class StatusUpdate(UpdateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CampusUpdate(UpdateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClasseUpdate(UpdateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')