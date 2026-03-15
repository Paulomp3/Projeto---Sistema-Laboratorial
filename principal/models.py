from django.db import models


class Permissoes(models.Model): # Não precisa de Crud
    id_permissoes = models.AutoField(db_column='ID_Permissoes', primary_key=True)
    permissao = models.CharField(db_column='Permissao', max_length=150)
    class Meta:
        db_table = 'Permissoes'
    def __str__(self):
        return self.permissao
        


class Usuarios(models.Model): # Verificar se precisa de CRUD, pois o sistema tem apenas um usuário admin
    id_usuarios = models.AutoField(db_column='ID_Usuarios', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=200)
    email = models.CharField(db_column='Email', unique=True, max_length=200)
    senha = models.CharField(db_column='Senha', max_length=100)
    id_permissoes = models.ForeignKey(Permissoes, models.DO_NOTHING, db_column='ID_Permissoes', blank=True, null=True)
    criado_em = models.DateTimeField(db_column='Criado_em', blank=True, null=True)
    atualizado_em = models.DateTimeField(db_column='Atualizado_em', blank=True, null=True)

    class Meta:
        db_table = 'Usuarios'
    
    def __str__(self):
        return self.nome


class Laboratorios(models.Model): # CRUD DE LABORATORIOS CONCLUIDO
    id_laboratorios = models.AutoField(db_column='ID_Laboratorios', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=150, blank=True, null=True)
    tipo = models.CharField(db_column='Tipo', max_length=150, blank=True, null=True)
    localizacao = models.CharField(db_column='Localizacao', max_length=150, blank=True, null=True)
    area = models.DecimalField(db_column='Area', max_digits=8, decimal_places=2, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Laboratorios'
    def __str__(self):
        return self.nome


class Agendamentos(models.Model): # 
    id_agendamentos = models.AutoField(db_column='ID_Agendamentos', primary_key=True)
    id_usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='ID_Usuarios')
    id_laboratorio = models.ForeignKey(Laboratorios, models.DO_NOTHING, db_column='ID_Laboratorio')
    tipo_de_atividade = models.TextField(db_column='Tipo_de_Atividade', blank=True, null=True)
    data_inicial = models.DateField(db_column='Data_Inicial', blank=True, null=True)
    data_final = models.DateField(db_column='Data_Final', blank=True, null=True)
    horario_inicio = models.TimeField(db_column='Horario_Inicio', blank=True, null=True)
    horario_final = models.TimeField(db_column='Horario_Final', blank=True, null=True)
    descricao_atividade = models.TextField(db_column='Descricao_Atividade', blank=True, null=True)

    class Meta:
        db_table = 'Agendamentos'


class Emprestimos(models.Model):
    id_emprestimos = models.AutoField(db_column='ID_Emprestimos', primary_key=True)
    nome_requerente = models.CharField(db_column='Nome_Requerente', max_length=200, blank=True, null=True)
    matricula = models.CharField(db_column='Matricula', max_length=100, blank=True, null=True)
    data_retirada = models.DateField(db_column='Data_Retirada')
    data_entrega = models.DateField(db_column='Data_Entrega')
    id_usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='ID_Usuarios', blank=True, null=True)

    class Meta:
        db_table = 'Emprestimos'
    def __str__(self):
        return self.nome_requerente


class EmprestimoExterno(models.Model):
    id_emprestimo = models.OneToOneField(Emprestimos, models.DO_NOTHING, db_column='ID_Emprestimo', primary_key=True)
    atividade = models.TextField(db_column='Atividade', blank=True, null=True)
    associacao = models.TextField(db_column='Associacao', blank=True, null=True)

    class Meta:
        db_table = 'Emprestimo_Externo'


class Material(models.Model):
    id_material = models.AutoField(db_column='ID_Material', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=150, blank=True, null=True)
    tipo = models.CharField(db_column='Tipo', max_length=150, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=100, blank=True, null=True)
    fabricante = models.CharField(db_column='Fabricante', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Material'
    def __str__(self):
        return self.nome


class MaterialEquipamentos(models.Model):
    id_material = models.OneToOneField(Material, models.DO_NOTHING, db_column='ID_Material', primary_key=True)
    patrimonio = models.CharField(db_column='Patrimonio', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Material_Equipamentos'



class MaterialVidrarias(models.Model):
    id_material = models.OneToOneField(Material, models.DO_NOTHING, db_column='ID_Material', primary_key=True)

    class Meta:
        db_table = 'Material_Vidrarias'
    


class MaterialReagentes(models.Model):
    id_material = models.OneToOneField(Material, models.DO_NOTHING, db_column='ID_Material', primary_key=True)
    lote = models.CharField(db_column='Lote', max_length=100, blank=True, null=True)
    validade = models.CharField(db_column='Validade', max_length=100)
    medida = models.CharField(db_column='Medida', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Material_Reagentes'



class MaterialConsumiveis(models.Model):
    id_material = models.OneToOneField(Material, models.DO_NOTHING, db_column='ID_Material', primary_key=True)

    class Meta:
        db_table = 'Material_Consumiveis'


class EstoqueLaboratorio(models.Model):
    id_estoque = models.AutoField(db_column='ID_Estoque', primary_key=True)
    id_laboratorio = models.ForeignKey(Laboratorios, models.DO_NOTHING, db_column='ID_Laboratorio')
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='ID_Material')
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)

    class Meta:
        db_table = 'Estoque_Laboratorio'


class MateriaisAgendamentos(models.Model):
    pk = models.CompositePrimaryKey('id_agendamentos', 'id_materiais')
    id_agendamentos = models.ForeignKey(Agendamentos, models.DO_NOTHING, db_column='ID_Agendamentos')
    id_materiais = models.ForeignKey(Material, models.DO_NOTHING, db_column='ID_Materiais')

    class Meta:
        db_table = 'Materiais_Agendamentos'


class EmprestimosMateriais(models.Model):
    pk = models.CompositePrimaryKey('id_material', 'id_emprestimos')
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='ID_Material')
    id_emprestimos = models.ForeignKey(Emprestimos, models.DO_NOTHING, db_column='ID_Emprestimos')

    class Meta:
        db_table = 'Emprestimos_Materiais'