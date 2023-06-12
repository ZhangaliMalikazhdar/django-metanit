from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.datetime)
