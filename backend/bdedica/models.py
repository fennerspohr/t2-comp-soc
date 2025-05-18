from django.db import models
from model_utils.models import TimeStampedModel #TimeStampedModel = os objetos sao criados automaticamente com colunas de data de criacao e edicaoSS

class Orientador(models.Model):
    nome = models.CharField(max_length=100)

class AtoInfracional(models.Model):
    nome = models.CharField(max_length=100)

class Adolescente(models.Model):

    SEXO_CHOICES = (
        (MASCULINO, "Masculino"),
        (FEMININO, "Feminino"),
        (OUTRO, "Outro")
    )

    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    data_nasc = models.DateField()
    nome_mae = models.CharField(max_length=100, blank=True)
    tem_CT = models.BooleanField()
    nome_CT = models.CharField(max_length=100, blank=True)
    sexo = models.IntegerFIeld(choices=SEXO_CHOICES)

    def save_API(dados):
        adolescente = Adolescente(cpf = dados['cpf'], nome = dados['cpf'], nome_social=dados['nome_social'],
                                  endereco= dados['endereco'], bairro=dados['bairro'], data_nasc=dados['data_nasc'],
                                  nome_mae=dados['nome_mae'], tem_CT=dados['tem_CT'], nome_CT=dados['nome_CT'], sexo=dados['sexo'])
        adolescente.save()

        contato = ContatoAdolescente(telefone=dados['telefone'], id_adolescente=adolescente)
        contato.save()

class ContatoAdolescente(TimeStampedModel):
    telefone = models.CharField(max_length=15)
    id_adolescente = models.ForeignKey(Adolescente, related_name="contato", on_delete=models.CASCADE)

class MSE(TimeStampedModel):

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
    infracao = models.ForeignKey(AtoInfracional)
    tipo_mse = models.IntegerField(choices=TIPOMSE_CHOICES)
    id_adolescente = models.ForeignKey(Adolescente)
    id_orientador = models.ForeignKey(Orientador)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    concluida = models.BooleanField()
    tipo_finalizacao = models.IntegerField(choices=TIPOFINALIZACAO_CHOICES, null=True)
    tipo_interrupcao = models.IntegerField(choices=TIPOINTERRUPCAO_CHOICES, null=True)
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
