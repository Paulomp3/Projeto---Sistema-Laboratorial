from django.shortcuts import render
from django.http import HttpResponse

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

def laboratorios(request):
    return render(request, 'pages/Laboratorios/laboratorios.html')

def agendamentos(request):
    return render(request, 'pages/Agendamentos/agendamentos.html')

def novo_agendamento(request):
    return render(request, 'pages/Agendamentos/novo_agendamento.html')

