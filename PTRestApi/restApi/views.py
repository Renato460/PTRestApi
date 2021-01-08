from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from  .serializers import TodoSerializer


class TodoList(APIView):
    """ Clase para el manejo de las peticiones """
    
    def get(self, request):
        """ CRUD GET lista todos los objetos del modelo y los retorna en formato JSON """
        todos= Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """ CRUD POST ingresa un objeto en formato JSON y lo convierte al modelo del programa """
        serializer = TodoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, nombre, format=None):
        """ CRUD busca un obtejo recibiendo el nombre de la Tarea luego lo actualiza"""
        todos = Todo.objects.get(nombre=nombre)
        serializer = TodoSerializer(todos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
