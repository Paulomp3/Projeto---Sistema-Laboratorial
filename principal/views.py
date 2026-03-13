from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'pages/login.html')
def busca_metodologias(request):
    return render(request, 'pages/busca_metodologias.html')
def cadastro(request):
    return render(request, 'pages/cadastro.html')
def dashboard(request):
    return render(request, 'pages/dashboard.html')
def emprestimo_externo(request):
    return render(request, 'pages/emprestimo_externo.html')
def emprestimo_interno(request):
    return render(request, 'pages/emprestimo_interno.html')
def emprestimos(request):
    return render(request, 'pages/emprestimos.html')
def inventario_equipamentos(request):
    return render(request, 'pages/inventario_equipamentos.html')
def laboratorios(request):
    return render(request, 'pages/laboratorios.html')
def novo_agendamento(request):
    return render(request, 'pages/novo_agendamento.html')
