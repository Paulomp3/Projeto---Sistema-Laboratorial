from django.urls import path
from principal import views


urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('novo_agendamento/', views.novo_agendamento, name='novo_agendamento'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('emprestimo_externo/', views.emprestimo_externo, name='emprestimo_externo'),
    path('emprestimo_interno/', views.emprestimo_interno, name='emprestimo_interno'),
    path('busca_metodologias/', views.busca_metodologias, name='busca_metodologias'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inventario_equipamentos/', views.inventario_equipamentos, name='inventario_equipamentos'),
    
]



