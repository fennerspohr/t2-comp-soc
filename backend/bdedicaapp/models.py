from django.db import models
from enum import Enum
# from model_utils.models import TimeStampedModel #TimeStampedModel = os objetos sao criados automaticamente com colunas de data de criacao e edicaoSS

class Orientador(models.Model):
    nome = models.CharField(max_length=100)

class AtoInfracional(models.Model):
    nome = models.CharField(max_length=100)

class Adolescente(models.Model):

    MASCULINO = 0 
    FEMININO = 1
    OUTRO = 2

    SEXO_CHOICES = [
        (MASCULINO, "Masculino"),
        (FEMININO, "Feminino"),
        (OUTRO, "Outro")
    ]

    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    data_nasc = models.DateField()
    nome_mae = models.CharField(max_length=100, blank=True)
    tem_CT = models.BooleanField()
    nome_CT = models.CharField(max_length=100, blank=True)
    sexo = models.IntegerField(choices=SEXO_CHOICES, default=OUTRO)

    def save_API(dados):
        dados = dados['form']
        adolescente = Adolescente(cpf = dados['cpf'], nome = dados['nome'], nome_social=dados['nome_social'],
                                  endereco= dados['endereco'], bairro=dados['bairro'], data_nasc=dados['data_nasc'],
                                  nome_mae=dados['nome_mae'], tem_CT=dados['tem_CT'], nome_CT=dados['nome_CT'], sexo=dados['sexo'])
        adolescente.save()

        if(len(dados['contatos']) > 0):
            for contato in dados['contatos']:
                c = ContatoAdolescente(telefone=contato, id_adolescente=adolescente)
                c.save()
    def update_API(dados):
        dados = dados['form']
        Adolescente.objects.get(dados['id']).update(
            cpf = dados['cpf'], nome = dados['nome'], nome_social=dados['nome_social'],
            endereco= dados['endereco'], bairro=dados['bairro'], data_nasc=dados['data_nasc'],
            nome_mae=dados['nome_mae'], tem_CT=dados['tem_CT'], nome_CT=dados['nome_CT'], sexo=dados['sexo']
        )

class ContatoAdolescente(models.Model):
    telefone = models.CharField(max_length=15)
    id_adolescente = models.ForeignKey(Adolescente, related_name="contato", on_delete=models.CASCADE)


class MSE(models.Model):

    LA = 0
    PSC = 1
    LA_PSC = 2

    CONCLUIDA = 0
    INTERROMPIDA = 1
    REGREDIDA = 2
    TRANSFERIDA = 3
    
    CASE = 0
    PENITENCIARIA = 1
    DESISTENCIA = 2
    EXTINTA = 3
    IDADE = 4
    REVOGADA = 5

    TIPOMSE_CHOICES = (
        (LA, "Liberdade Assistida"),
        (PSC, "Prestação de Serviços à Comunidade"),
        (LA_PSC, "LA com PSC")
    )
        
    TIPOFINALIZACAO_CHOICES = (
        (CONCLUIDA, "Concluída"),
        (INTERROMPIDA, "Interrompida"),
        (TRANSFERIDA, "Transferida"),
        (REGREDIDA, "Regredida")
    )

    TIPOINTERRUPCAO_CHOICES = (
        (CASE, "Case"),
        (PENITENCIARIA, "PRSM ou outra penitenciária"),
        (DESISTENCIA, "Desistência"),
        (EXTINTA, "Extinta pelo Judiciário (prescrição)"),
        (IDADE, "Idade"),
        (REVOGADA, "Revogada (não cumpre)")
    )
  
    processo_num = models.CharField(max_length=15)
    infracao = models.ForeignKey(AtoInfracional, on_delete=models.RESTRICT)
    tipo_mse = models.IntegerField(choices=TIPOMSE_CHOICES)
    id_adolescente = models.ForeignKey(Adolescente, on_delete=models.RESTRICT)
    id_orientador = models.ForeignKey(Orientador,on_delete=models.RESTRICT)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    concluida = models.BooleanField()
    tipo_finalizacao = models.IntegerField(choices=TIPOFINALIZACAO_CHOICES, blank=True, null=True)
    tipo_interrupcao = models.IntegerField(choices=TIPOINTERRUPCAO_CHOICES, blank=True, null=True)
    caixa_baixa_num = models.IntegerField()

    def save_API(dados):
        adolescente = Adolescente.objects.get(id=dados['id_adolescente'])
        orientador = Orientador.objects.get(id=dados['id_orientador'])
        infracao = AtoInfracional.objects.get(id=dados['infracao'])

        mse = MSE(processo_num=dados['processo_num'], infracao=infracao, tipo_mse=dados['tipo_mse'],
                  id_adolescente=adolescente, id_orientador=orientador, data_inicio=dados['data_inicio'],
                  data_fim=dados['data_fim'], concluida=dados['concluida'], tipo_finalizacao=dados['tipo_finalizacao'],
                  tipo_interrupcao=dados['tipo_interrupcao'], caixa_baixa_num=dados['caixa_baixa_num'])
        mse.save()
    def update_API(dados):
        adolescente = Adolescente.objects.get(id=dados['id_adolescente'])
        orientador = Orientador.objects.get(id=dados['id_orientador'])
        infracao = AtoInfracional.objects.get(id=dados['infracao'])
        MSE.objects.get(id=dados['id']).update(
            processo_num=dados['processo_num'], infracao=infracao, tipo_mse=dados['tipo_mse'],
            id_adolescente=adolescente, id_orientador=orientador, data_inicio=dados['data_inicio'],
            data_fim=dados['data_fim'], concluida=dados['concluida'], tipo_finalizacao=dados['tipo_finalizacao'],
            tipo_interrupcao=dados['tipo_interrupcao'], caixa_baixa_num=dados['caixa_baixa_num']
        )

