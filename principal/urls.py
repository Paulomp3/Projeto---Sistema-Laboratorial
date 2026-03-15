from django.urls import path
from principal import views


urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('busca_metodologias/', views.busca_metodologias, name='busca_metodologias'),
    # ----- CRUD DE LABORATORIOS -----
    path('laboratorios/', views.laboratorios_listar, name='laboratorios_listar'), # Lista os laboratorios do sistema
    path('laboratorios/form/', views.laboratorios_form, name='laboratorios_form'), # Exibe o formulário para criar um novo laboratório e processa a criação do laboratório
    path('laboratorios/editar/<int:id>/', views.laboratorios_editar, name='laboratorios_editar'), # Exibe o formulário para editar um laboratório existente e processa a edição do laboratório
    path('laboratorios/deletar/<int:id>/', views.laboratorios_delete, name='laboratorios_delete'), # Exclui um laboratório específico com base no ID fornecido
    # ----- CRUD DE LABORATORIOS - FIM -----
    
    # ----- CRUD DE EMPRESTIMOS -----
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('emprestimo_externo/', views.emprestimo_externo, name='emprestimo_externo'),
    path('emprestimo_interno/', views.emprestimo_interno, name='emprestimo_interno'),
    # ----- CRUD DE EMPRESTIMOS - FIM -----
    
    # ----- CRUD DE MATERIAIS -----
    path('cadastro/', views.material_cadastro, name='cadastro'),
    path('equipamentos/', views.Equipamentos, name='inventario_equipamentos'),
    path('consumiveis/', views.Consumiveis, name='inventario_consumiveis'),
    path('reagentes/', views.Reagentes, name='inventario_reagentes'),
    path('vidrarias/', views.Vidrarias, name='inventario_vidrarias'),
    path('epis/', views.Epis, name='inventario_epis'),  
    # ----- CRUD DE MATERIAIS - FIM -----
    
]



