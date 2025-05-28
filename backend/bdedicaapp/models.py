from django.db import models
from enum import Enum
# from model_utils.models import TimeStampedModel #TimeStampedModel = os objetos sao criados automaticamente com colunas de data de criacao e edicaoSS

class Orientador(models.Model):
    nome = models.CharField(max_length=100)

class AtoInfracional(models.Model):
    nome = models.CharField(max_length=100)


class Sexo(Enum):
    MASCULINO="Masculino"
    FEMININO = "Feminino"
    OUTRO = "Outro"

class Adolescente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    data_nasc = models.DateField()
    nome_mae = models.CharField(max_length=100, blank=True)
    tem_CT = models.BooleanField()
    nome_CT = models.CharField(max_length=100, blank=True)
    sexo = models.IntegerField(choices=[(sexo.value, sexo.name) for sexo in Sexo])

    def save_API(dados):
        adolescente = Adolescente(cpf = dados['cpf'], nome = dados['cpf'], nome_social=dados['nome_social'],
                                  endereco= dados['endereco'], bairro=dados['bairro'], data_nasc=dados['data_nasc'],
                                  nome_mae=dados['nome_mae'], tem_CT=dados['tem_CT'], nome_CT=dados['nome_CT'], sexo=dados['sexo'])
        adolescente.save()

        contato = ContatoAdolescente(telefone=dados['telefone'], id_adolescente=adolescente)
        contato.save()

class ContatoAdolescente(models.Model):
    telefone = models.CharField(max_length=15)
    id_adolescente = models.ForeignKey(Adolescente, related_name="contato", on_delete=models.CASCADE)

class TipoMSE(Enum):
    LA ="Liberdade Assistida"
    PSC="Prestação de Serviços à Comunidade"
    LA_PSC="LA com PSC"

class TipoFinalizacao(Enum):
    CONCLUIDA="Concluída"
    INTERROMPIDA="Interrompida"
    TRANSFERIDA="Transferida"
    REGREDIDA="Regredida"

class TipoInterrupcao(Enum):
    CASE="Case"
    PENITENCIARIA="PRSM ou outra penitenciária"
    DESISTENCIA="Desistência"
    EXTINTA= "Extinta pelo Judiciário (prescrição)"
    IDADE="Idade"
    REVOGADA="Revogada (não cumpre)"

class MSE(models.Model):
  
    processo_num = models.CharField(max_length=15)
    infracao = models.ForeignKey(AtoInfracional, on_delete=models.RESTRICT)
    tipo_mse = models.IntegerField(choices=[(tipo.value, tipo.name) for tipo in TipoMSE])
    id_adolescente = models.ForeignKey(Adolescente, on_delete=models.RESTRICT)
    id_orientador = models.ForeignKey(Orientador,on_delete=models.RESTRICT)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    concluida = models.BooleanField()
    tipo_finalizacao = models.IntegerField(choices=[(tipo.value, tipo.name) for tipo in TipoFinalizacao], null=True)
    tipo_interrupcao = models.IntegerField(choices=[(tipo.value, tipo.name) for tipo in TipoInterrupcao], null=True)
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
