from rest_framework import serializers
from .models import Adolescente, ContatoAdolescente, MSE, AtoInfracional, Orientador

class OrientadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientador
        fields = all

class AtoInfracionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtoInfracional
        fields = all

class AdolescenteSerializer(serializers.ModelSerializer):
    sexo_str = serializers.CharField(source='get_sexo_display')
    class Meta:
        model = Adolescente
        fields = ['id', 'cpf', 'nome', 'nome_social', 'endereco', 'bairro', 'data_nasc',
                  'nome_mae', 'tem_CT', 'nome_CT', 'sexo', 'sexo_str']
        
class ContatoAdolescenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoAdolescente
        fields = all

class MSESerializer(serializers.ModelSerializer):
    tipo_mse_str = serializers.CharField(source='get_tipo_mse_display')
    tipo_finalizacao_str = serializers.CharField(source='get_tipo_finalizacao_display')
    tipo_interrupcao_str = serializers.CharField(source='get_tipo_interrupcao_display')
    id_orientador = OrientadorSerializer()
    id_adolescente = AdolescenteSerializer()
    infracao = AtoInfracionalSerializer()
    class Meta:
        model = MSE
        fields = (all, 'tipo_mse_str', 'tipo_finalizacao_str', 'tipo_interrupcao_str')