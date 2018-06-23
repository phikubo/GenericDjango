from django.db import models

# Create your models here.

class pregunta(models.Model):
    pregunta_texto= models.CharField(max_length=100)
    pub_calendario= models.DateTimeField('Fecha de publicacion')
    def __str__(self):
        return self.pregunta_texto

class eleccion(models.Model):
    preguntas= models.ForeignKey(pregunta,on_delete=models.CASCADE)
    eleccion_texto= models.CharField(max_length=100)
    votos= models.IntegerField(default=0)
    def __str__(self):
        return self.eleccion_texto
    