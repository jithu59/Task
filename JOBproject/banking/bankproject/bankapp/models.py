from django.db import models


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=40)

    def __str__(self):
        return self.city


class Region(models.Model):
    name = models.CharField(max_length=40)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.district


class Field(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.email

