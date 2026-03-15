from unittest import case

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def login(request):
    return render(request, 'pages/Login/login.html')
def dashboard(request):
    return render(request, 'pages/Dashboard/dashboard.html')
def busca_metodologias(request):

    return render(request, 'pages/Metodologias/busca_metodologias.html')
# ---- CRUD DE MATERIAIS ----
def material_cadastro(request):
    match request.method:
        case 'GET':
            return render(request, 'pages/Materiais/cadastro.html')
        case 'POST':
            nome = request.POST.get('nome')
            fabricante = request.POST.get('fabricante')
            tipo = request.POST.get('tipo')
            status = request.POST.get('status')

            materiais = Material(nome=nome, fabricante=fabricante, tipo=tipo, status=status)
            materiais.save()
            return redirect('cadastro')
def Equipamentos(request):
    match request.method:
        case 'GET':
            materiais = Material.objects.all()
            return render(request, 'pages/Materiais/equipamentos.html', {'materiais': materiais})
def Consumiveis(request):
    match request.method:
        case 'GET':
            materiais = Material.objects.all()
            return render(request, 'pages/Materiais/consumiveis.html', {'materiais': materiais})
def Reagentes(request):
    match request.method:
        case 'GET':
            materiais = Material.objects.all()
            return render(request, 'pages/Materiais/reagentes.html', {'materiais': materiais})
def Vidrarias(request):
    match request.method:
        case 'GET':
            materiais = Material.objects.all()
            return render(request, 'pages/Materiais/vidrarias.html', {'materiais': materiais})
def Epis(request):
    match request.method:
        case 'GET':
            materiais = Material.objects.all()
            return render(request, 'pages/Materiais/epis.html', {'materiais': materiais})
# ---- CRUD DE MATERIAIS - FIM ----

#----- CRUD DE EMPRESTIMOS ----
def emprestimo_externo(request):
    return render(request, 'pages/Emprestimos/emprestimo_externo.html')
def emprestimo_interno(request):
    return render(request, 'pages/Emprestimos/emprestimo_interno.html')
def emprestimos(request):
    return render(request, 'pages/Emprestimos/emprestimos.html')
# ----- CRUD DE EMPRESTIMOS - FIM ----

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
def laboratorios_delete(request, id):
    match request.method: # Match para verificar o método HTTP da requisição
        case 'GET': # Se for uma requisição POST, processa a exclusão do laboratório com base no ID fornecido
          lab = Laboratorios.objects.get(id_laboratorios=id) 
          return render(request, 'pages/Laboratorios/delete.html', {'lab': lab}) # Renderiza a página de confirmação de exclusão, passando o ID do laboratório como contexto
        case 'POST':
            lab = Laboratorios.objects.get(id_laboratorios=id) # Consulta para obter o laboratório específico com base no ID fornecido
            lab.delete() # Exclui o laboratório do banco de dados
            return redirect('laboratorios_listar') # Redireciona para a página de listagem de laboratórios após excluir o laboratório      
def laboratorios_editar(request, id):
    match request.method:
        case 'GET': # Se for uma requisição GET, renderiza o formulário para editar um laboratório existente, preenchendo os campos do formulário com os dados atuais do laboratório
            lab = Laboratorios.objects.get(id_laboratorios=id) # Consulta para obter o laboratório específico com base no ID fornecido
            return render(request, 'pages/Laboratorios/form.html', {'lab': lab}) # Renderiza a página de formulário para edição, passando o laboratório como contexto para preencher os campos do formulário com os dados existentes
        case 'POST': # Se for uma requisição POST, processa os dados enviados pelo formulário para editar o laboratório existente
            lab = Laboratorios.objects.get(id_laboratorios=id) 
            nome = request.POST.get('nome')
            tipo = request.POST.get('tipo')
            localizacao = request.POST.get('localizacao')
            area  = request.POST.get('area')
            status = request.POST.get('status')
            # Atualiza os campos do laboratório com os novos dados obtidos do formulário e salva as alterações no banco de dados
            lab.nome = nome 
            lab.tipo = tipo
            lab.localizacao = localizacao
            lab.area = area
            lab.status = status
            lab.save()
            return redirect('laboratorios_listar')
# ----- CRUD DE LABORATORIOS - FIM -----      

# ----- CRUD DE AGENDAMENTOS -----
def agendamentos_listar(request):
    match request.method:
        case 'GET':
            agendamentos = Agendamentos.objects.all()
            return render(request, 'pages/Agendamentos/agendamentos_listar.html',{'agendamentos': agendamentos})
        
def agendamentos_form(request):
    match request.method:
        case 'GET': # Se for uma requisição GET, renderiza o formulário para criar um novo agendamento
            laboratorios = Laboratorios.objects.all() # Consulta para obter todos os laboratórios do banco de dados
            usuarios = Usuarios.objects.all() # Consulta para obter todos os usuários do banco de dados
            return render(request, 'pages/Agendamentos/agendamentos_form.html', {'laboratorios': laboratorios, 'usuarios': usuarios})
        case 'POST': # Se for uma requisição POST, processa os dados enviados pelo formulário para criar um novo agendamento
            id_laboratorio = request.POST.get('id_laboratorios')
            id_usuario = request.POST.get('id_usuarios')
            tipo_de_atividade = request.POST.get('tipo_de_atividade')
            descricao_atividade = request.POST.get('descricao_atividade')
            data_inicial = request.POST.get('data_inicial')
            data_final = request.POST.get('data_final')
            horario_inicio = request.POST.get('horario_inicio')
            horario_final = request.POST.get('horario_final')

            laboratorios = Laboratorios.objects.get(id_laboratorios=id_laboratorio) # Consulta para obter o laboratório específico com base no ID fornecido
            usuarios = Usuarios.objects.get(id_usuarios=id_usuario) # Consulta para obter o usuário específico com base no ID fornecido
            
            agendamento = Agendamentos(
                id_laboratorio=laboratorios, 
                id_usuarios=usuarios, 
                tipo_de_atividade=tipo_de_atividade, 
                descricao_atividade=descricao_atividade, 
                data_inicial=data_inicial, 
                data_final=data_final, 
                horario_inicio=horario_inicio, 
                horario_final=horario_final
            )
            agendamento.save()
            return redirect('agendamentos_listar') # Redireciona para a página de listagem de agendamentos após criar um novo agendamento
     
def agendamentos_delete(request,id):
    match request.method:
        case 'GET':
            agendamentos = Agendamentos.objects.get(id_agendamentos = id)
            return render(request, 'pages/Agendamentos/agendamentos_delete.html', {'ag': agendamentos})
        case 'POST':
            agendamentos = Agendamentos.objects.get(id_agendamentos = id)
            agendamentos.delete()
            return redirect(agendamentos_listar)

def agendamentos_editar(request, id):
    match request.method:
        case 'GET':
            agendamentos = Agendamentos.objects.get(id_agendamentos = id)
            laboratorios = Laboratorios.objects.all()
            usuarios = Usuarios.objects.all()
            return render(request, 'pages/Agendamentos/agendamentos_form.html', {'ag': agendamentos , 'laboratorios': laboratorios , 'usuarios': usuarios})
        case 'POST': 
            agendamentos = Agendamentos.objects.get(id_agendamentos =id)
            
            id_laboratorio = request.POST.get('id_laboratorios')
            id_usuario = request.POST.get('id_usuarios')
            tipo_de_atividade = request.POST.get('tipo_de_atividade')
            descricao_atividade = request.POST.get('descricao_atividade')
            data_inicial = request.POST.get('data_inicial')
            data_final = request.POST.get('data_final')
            horario_inicio = request.POST.get('horario_inicio')
            horario_final = request.POST.get('horario_final')
             
            agendamentos.id_laboratorio = Laboratorios.objects.get(id_laboratorios = id_laboratorio)
            agendamentos.id_usuarios = Usuarios.objects.get(id_usuarios = id_usuario )
            agendamentos.tipo_de_atividade = tipo_de_atividade
            agendamentos.descricao_atividade = descricao_atividade
            agendamentos.data_inicial = data_inicial
            agendamentos.data_final = data_final
            agendamentos.horario_inicio = horario_inicio
            agendamentos.horario_final = horario_final

            agendamentos.save()
            return redirect('agendamentos_listar')

# -------- CRUD DE AGENDAMENTOS - FIM - ----

