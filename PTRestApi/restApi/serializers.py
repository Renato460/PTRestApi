from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    """Clase que transforma los datos del modelo a formato JSON"""
    class Meta:
        model = Todo
        fields= ['nombre', 'estado', 'descripcion']
