from django.db import models

class BaseRate(models.Model):
    date = models.DateField( blank = False, null = False)
    base = models.CharField(max_length=3, null = False)

    def __str__(self):
        return self.date


class Rate(models.Model):
    rate = models.CharField(max_length=3, null = False)
    valor = models.FloatField()
    base_rate=models.ForeignKey(BaseRate, null=True, on_delete=models.CASCADE, related_name="rates")

    def __str__(self):
        return '%s:%f'%   (self.rate,self.valor)


class Currency(models.Model):
    sigla = models.CharField(max_length=3, null = False)
    name = models.CharField(max_length=30, null = False)
    symbol = models.CharField(max_length=10, null = False)
   
    def __str__(self):
        return '%s:%s'%   (self.sigla,self.name)