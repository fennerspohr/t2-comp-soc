from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MSE, Adolescente, Orientador, AtoInfracional
from .serializers import MSESerializer, AdolescenteSerializer, OrientadorSerializer, AtoInfracionalSerializer

class MSEAPIView(APIView):
    def get(self, request, *args, **kwargs):
        mse = MSE.objects.all()
        serializer = MSESerializer(mse, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        dados = request.data
        MSE.save_API(dados)
        return Response(status=status.HTTP_201_CREATED)
    
class AdolescenteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        adolescente = Adolescente.objects.all()
        serializer = AdolescenteSerializer(adolescente, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        dados = request.data
        Adolescente.save_API(dados)
        return Response(status=status.HTTP_201_CREATED)
    
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