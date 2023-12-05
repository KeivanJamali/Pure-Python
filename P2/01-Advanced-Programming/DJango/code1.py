from django.db import models


class Person(models.Model):
    SHIRT_SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    age = models.IntegerField()

class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    # type = models.CharField(max_length=30, choices=RunnerType.choices)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    color = models.CharField(max_length=30)

