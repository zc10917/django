# -*- coding: <UTF-8> -*-
from django.db import models


# Create your models here.
# class Student1(models.Model):
#     name = models.CharField(max_length=50)
class oc(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    age1 = models.IntegerField(default=10)
    age2 = models.IntegerField(default=10)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['age']
