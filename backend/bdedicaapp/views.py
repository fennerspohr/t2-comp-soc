from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MSE, Adolescente, Orientador, AtoInfracional
from .serializers import MSESerializer, AdolescenteSerializer, OrientadorSerializer, AtoInfracionalSerializer, CountSerializer

class CountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        mse = MSE.objects.count()
        adolescente = Adolescente.objects.count()
        orientador = Orientador.objects.count()
        serializer = CountSerializer({"mse":mse, "adolescente":adolescente, "orientador":orientador})
        return Response(serializer.data)


class MSEAPIView(APIView):
    def get(self, request, *args, **kwargs):
        mse = {}
        if(request.GET.get('id')):
            mse = MSE.objects.get(id=request.GET.get('id'))
            serializer = MSESerializer(mse, many=False)

        else:
            mse = MSE.objects.all()
            serializer = MSESerializer(mse, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        dados = request.data
        MSE.save_API(dados)
        return Response(status=status.HTTP_201_CREATED)
    
class MSEUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        dados = request.data
        MSE.update_API(dados)
        return Response(status=status.HTTP_200_OK)

    
class MSEFilterView(APIView):
    def get(self, request, *args, **kwargs):
        dados = {}
        status = ''

        if(request.GET.get('status')):
            if request.GET.get('status').lower() == 'true':
                status = True
            elif request.GET.get('status').lower() == 'false':
                status = False

        if(request.GET.get('ano') and request.GET.get('status') and request.GET.get('busca')):
            if(request.GET.get('busca').isnumeric()):
                print("numero")
                dados = MSE.objects.filter(data_inicio__year=request.GET.get('ano'), id_adolescente__cpf__contains=request.GET.get('busca'), concluida=status)
            else:
                print("oi")
                dados = MSE.objects.filter(data_inicio__year=request.GET.get('ano'), id_adolescente__nome__contains=request.GET.get('busca'), concluida=status)
        elif(request.GET.get('ano') and request.GET.get('status')):
            dados = MSE.objects.filter(data_inicio__year=request.GET.get('ano'), concluida=status)
        elif(request.GET.get('ano') and request.GET.get('busca')):
            if(request.GET.get('busca').isnumeric()):
                dados = MSE.objects.filter(data_inicio__year=request.GET.get('ano'), id_adolescente__cpf__contains=request.GET.get('busca'))
            else:
                dados = MSE.objects.filter(data_inicio__year=request.GET.get('ano'), id_adolescente__nome__contains=request.GET.get('busca'))
        elif(request.GET.get('ano')):
            dados = MSE.objects.filter(data_inicio__year=request.GET.get('ano'))
        elif(request.GET.get('status') and request.GET.get('busca')):
            if(request.GET.get('busca').isnumeric()):
                dados = MSE.objects.filter(concluida=status, id_adolescente__cpf__contains=request.GET.get('busca'))
            else:
                dados = MSE.objects.filter(concluida=status, id_adolescente__nome__contains=request.GET.get('busca'))
        elif(request.GET.get('status')):
            dados = MSE.objects.filter(concluida=status)
        elif(request.GET.get('busca')):
            if(request.GET.get('busca').isnumeric()):
                dados = MSE.objects.filter(id_adolescente__cpf__contains=request.GET.get('busca'))
            else:
                dados = MSE.objects.filter(id_adolescente__nome__contains=request.GET.get('busca'))
        serializer = MSESerializer(dados, many=True)
        print(dados)
        return Response(serializer.data)
    
class AdolescenteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        adolescente = {}
        if(request.GET.get('id')):
            adolescente = Adolescente.objects.get(id=request.GET.get('id'))
            serializer = AdolescenteSerializer(adolescente, many=False)
        else:
            adolescente = Adolescente.objects.all()
            serializer = AdolescenteSerializer(adolescente, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        dados = request.data
        Adolescente.save_API(dados)
        return Response(status=status.HTTP_201_CREATED)
    
class AdolescenteFiltroView(APIView):
    def get(self, request, *args, **kwargs):
        dados = {}

        busca = request.GET.get('busca')
        sexo = request.GET.get('sexo')

        if (busca and sexo):
            if(busca.isnumeric()):
                dados = Adolescente.objects.filter(cpf__contains=request.GET.get('busca'), sexo__iexact=sexo)
            else: 
                dados = Adolescente.objects.filter(nome__contains=request.GET.get('busca'), sexo__iexact=sexo)
        elif busca:
            if(busca.isnumeric()):
                dados = Adolescente.objects.filter(cpf__contains=request.GET.get('busca'))
            else: 
                dados = Adolescente.objects.filter(nome__contains=request.GET.get('busca'))
        elif sexo:
            dados = Adolescente.objects.filter(sexo__iexact=sexo)
        else:
            dados = Adolescente.objects.all()
        serializer = AdolescenteSerializer(dados, many=True)
        print(dados)
        return Response(serializer.data)

class AdolescenteUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        dados = request.data
        Adolescente.update_API(dados)
        return Response(status=status.HTTP_200_OK)
    
class OrientadorAPIView(APIView):
    def get(self, request, *args, **kwargs):
        orientador = Orientador.objects.all()
        serializer = OrientadorSerializer(orientador, many=True)
        return Response(serializer.data)
    
class AtoInfracionalAPIView(APIView):
    def get(self, request, *args, **kwargs):
        ato = AtoInfracional.objects.all()
        serializer = AtoInfracionalSerializer(ato, many=True)
        return Response(serializer.data)