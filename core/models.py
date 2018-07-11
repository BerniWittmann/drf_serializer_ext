from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
