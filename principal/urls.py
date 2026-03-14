from django.urls import path
from principal import views


urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # ----- CRUD DE LABORATORIOS -----
    path('laboratorios/', views.laboratorios_listar, name='laboratorios_listar'), # Lista os laboratorios do sistema
    path('laboratorios/form/', views.laboratorios_form, name='laboratorios_form'), # Exibe o formulário para criar um novo laboratório e processa a criação do laboratório 
    # ----- CRUD DE LABORATORIOS - FIM -----
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('novo_agendamento/', views.novo_agendamento, name='novo_agendamento'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('emprestimo_externo/', views.emprestimo_externo, name='emprestimo_externo'),
    path('emprestimo_interno/', views.emprestimo_interno, name='emprestimo_interno'),
    path('busca_metodologias/', views.busca_metodologias, name='busca_metodologias'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inventario_equipamentos/', views.inventario_equipamentos, name='inventario_equipamentos'),
    
]



