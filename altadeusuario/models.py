from django.db import models

class AltaUsuario(models.Model):
    identificacion = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Puesto = models.CharField(max_length=50)
    Horario = models.CharField(max_length=50)
    Descanso = models.CharField(max_length=50)
    perfil = (('usuariotecnico',"Usuario Técnico"),
           ('usuarioadministrador',"Usuario Administrador"))
    Perfiles = models.CharField(max_length=30, choices= perfil, default="usuarioadministrador")
    def __str__(self):
        return self.Nombre
# Create your models here.
