from django.db import models
from .functions import validate_CPF

# Create your models here.

class AnoEscolar(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Anos Escolares"
        verbose_name = "Ano Escolar"
        ordering = ['id']

    nome = models.CharField(unique=True, max_length=50)
    dt_inclusao = models.DateTimeField(auto_now_add=True)



class Curso(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    nome = models.CharField(unique=True, max_length=50)
    dt_inclusao = models.DateTimeField(auto_now_add=True)



class OutroCurso(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Outros Cursos"
        verbose_name = "Outro Curso"
        ordering = ['nome']

    nome = models.CharField(unique=True, max_length=50)
    dt_inclusao = models.DateTimeField(auto_now_add=True)



class Candidato(models.Model):
    JACURSOU = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    RETORNO_PRESENCIAL = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    def __str__(self):
        return '%s - %s' % (self.nome, self.cpf)

    class Meta:
        ordering = ['nome']

    nome = models.CharField(max_length=60, db_index=True)
    dt_nascimento = models.DateField('Data Nascimento', db_index=True)
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_CPF], verbose_name='CPF')
    email = models.CharField(max_length=250, blank=True, null=True, verbose_name='E-Mail')
    endereco = models.CharField(max_length=250, verbose_name='Endereço')
    bairro = models.CharField(max_length=250)
    escola = models.CharField(max_length=250)
    anoescolar = models.ForeignKey(AnoEscolar, on_delete=models.PROTECT, verbose_name='Ano Escolar')
    celular = models.CharField(max_length=11, blank=True, null=True)
    nome_responsavel1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nome do Responsável 1')
    grau_parentesco1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Grau do Parentesco 1')
    celular_1 = models.CharField(max_length=11, blank=True, null=True, verbose_name='Celular do Responsável 1')
    nome_responsavel2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nome do Responsável 2')
    grau_parentesco2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Grau do Parentesco 2')
    celular_2 = models.CharField(max_length=11, blank=True, null=True, verbose_name='Celular do Responsável 2')
    ja_cursou = models.CharField(max_length=1, choices=JACURSOU, verbose_name='O(A) aluno(a) já frequentou algum curso na Oficina Escola ou nos Pontos de Cultura?')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name='Curso Desejado')
    outro_curso = models.ManyToManyField(OutroCurso, verbose_name='Quais outros cursos você gostaria de ver disponíveis na Oficina Escola de Artes e nos Pontos de Cultura?', blank=True)
    retorno_presencial = models.CharField(max_length=1, choices=RETORNO_PRESENCIAL, verbose_name="Mediante o retorno das aulas presenciais seguindo todos os protocolos de segurança da vigilância sanitária, o aluno está autorizado a frequentá-las?")
    dt_inclusao = models.DateTimeField(auto_now_add=True)



class Aluno(models.Model):

    class Meta:
        ordering = ['candidato']

    def __str__(self):
        return '%s' % (self.candidato)

    candidato = models.OneToOneField(Candidato, on_delete=models.CASCADE)
    email_google = models.CharField(max_length=250, verbose_name='E-Mail no Google')
    ativo = models.BooleanField(default=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')



class Instrutor(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Instrutores"

    nome = models.CharField(unique=True, max_length=60)
    dt_inclusao = models.DateTimeField(auto_now_add=True)



class Turma(models.Model):
    def __str__(self):
        return '%s - %s' % (self.curso, self.id)

    class Meta:
        ordering = ['curso']

    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True)



class Turma_Aluno(models.Model):
    def __str__(self):
        return '%s - %s' % (self.turma, self.aluno)

    class Meta:
        ordering = ['turma', 'aluno']
        verbose_name_plural = "Turmas/Alunos"
        verbose_name = "Turma/Alunos"
        unique_together = ('turma', 'aluno')

    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    aluno = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
