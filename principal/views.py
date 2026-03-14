from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def login(request):
    return render(request, 'pages/Login/login.html')

def busca_metodologias(request):
    return render(request, 'pages/Metodologias/busca_metodologias.html')

def cadastro(request):
    return render(request, 'pages/Inventario/cadastro.html')

def dashboard(request):
    return render(request, 'pages/Dashboard/dashboard.html')

def emprestimo_externo(request):
    return render(request, 'pages/Emprestimos/emprestimo_externo.html')

def emprestimo_interno(request):
    return render(request, 'pages/Emprestimos/emprestimo_interno.html')

def emprestimos(request):
    return render(request, 'pages/Emprestimos/emprestimos.html')

def inventario_equipamentos(request):
    return render(request, 'pages/Inventario/inventario_equipamentos.html')
# ----- CRUD DE LABORATORIOS -----
def laboratorios_listar(request):
    match request.method:
        case 'GET':
            lab = Laboratorios.objects.all() # Consulta para obter todos os laboratórios do banco de dados
            return render(request, 'pages/Laboratorios/listar.html', {'laboratorios': lab}) # Renderiza a página de listagem de laboratórios, passando os laboratórios como contexto
def laboratorios_form(request):

    match request.method: # Match para verificar o método HTTP da requisição
        case 'GET':  # Se for uma requisição GET, renderiza o formulário para criar um novo laboratório
            return render(request, 'pages/Laboratorios/form.html')
        case 'POST': # Se for uma requisição POST, processa os dados enviados pelo formulário para criar um novo laboratório
           nome = request.POST.get('nome')
           tipo = request.POST.get('tipo')
           localizacao = request.POST.get('localizacao')
           area  = request.POST.get('area')
           status = request.POST.get('status')

           lab = Laboratorios(nome=nome, tipo=tipo, localizacao=localizacao, area=area, status=status)# Cria uma nova instância do modelo Laboratorios com os dados obtidos do formulário
           lab.save() 
           return redirect('laboratorios_listar') # Redireciona para a página de listagem de laboratórios após criar um novo laboratório
               
# ----- CRUD DE LABORATORIOS - FIM -----      
def agendamentos(request):
    return render(request, 'pages/Agendamentos/agendamentos.html')

def novo_agendamento(request):
    return render(request, 'pages/Agendamentos/novo_agendamento.html')

