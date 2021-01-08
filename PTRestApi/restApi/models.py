from django.db import models

class Todo(models.Model):
    nombre=models.CharField(max_length=30)
    estado=models.BooleanField(default=False)
    descripcion= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
