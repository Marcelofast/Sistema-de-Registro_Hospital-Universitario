from django.db import models

# Create your models here.

class pre_registro_paciente(models.Model):
    
    DatosGenerales = models.CharField(max_length=400)
    AntecedentesPersonales = models.SlugField(max_length=400)
    AntecedentesFamiliares = models.TextField(max_length=400)