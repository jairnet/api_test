from django.db import models
from apps.company.models import Company
# from rest_framework.authtoken.models import Token


class Program(models.Model):
    IDProgramacion = models.CharField(max_length=32, default='')
    NoPrescripcion = models.CharField(max_length=20, default='')
    TipoTec = models.CharField(max_length=1, default='')
    ConTec = models.CharField(max_length=2, default='')
    TipoIDPaciente = models.CharField(max_length=2, default='')
    NoIdPaciente = models.CharField(max_length=17, default='')
    NoEntrega = models.CharField(max_length=2, default='')
    FecMaxEnt = models.CharField(max_length=10, default='')
    TipoIDSedeProv = models.CharField(max_length=2, default='')
    NoIDSedeProv = models.CharField(max_length=9, default='')
    CodSedeProv = models.CharField(max_length=15, default='')
    CodSerTecAEntregar = models.CharField(max_length=20, default='')
    CantTotAEntregar = models.CharField(max_length=10, default='')
    FecProgramacion = models.CharField(max_length=16, default='')
    EstProgramacion = models.CharField(max_length=16, default='')
    FechaAnulacion = models.CharField(max_length=16, default='')

    class Meta:
        ordering = ["NoPrescripcion"]

    def __str__(self):
        return self.NoPrescripcion

