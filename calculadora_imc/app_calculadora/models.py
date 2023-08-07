from django.db import models

class Calculo(models.Model):
    id_calculo = models.AutoField(primary_key=True)
    peso = models.IntegerField()
    altura = models.IntegerField()
