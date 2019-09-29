from django.db import models
from apps.company.models import Company
# from rest_framework.authtoken.models import Token


class Address(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    date_address = models.DateField(blank=True)

    NoPrescripcion = models.CharField(max_length=20, default='')
    TipoTec = models.CharField(max_length=1, default='')
    ConTec = models.CharField(max_length=2, default='')
    TipoIdPaciente = models.CharField(max_length=2, default='')
    NoIdPaciente = models.CharField(max_length=17, default='')
    NoEntrega = models.CharField(max_length=2, default='')
    NoSubEntrega = models.CharField(max_length=2, default='')
    TipoIDProv = models.CharField(max_length=2, default='')
    NoIDProv = models.CharField(max_length=17, default='')
    CodMunEnt = models.CharField(max_length=5, default='')
    FecMaxEnt = models.CharField(max_length=10, default='')
    CantTotAEntregar = models.CharField(max_length=10, default='')
    DirPaciente = models.CharField(max_length=80, default='')
    CodSerTecAEntregar = models.CharField(max_length=20, default='')

    class Meta:
        ordering = ["NoPrescripcion"]

    def __str__(self):
        return self.NoPrescripcion
