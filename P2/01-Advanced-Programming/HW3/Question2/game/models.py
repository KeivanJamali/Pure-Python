from django.core import validators
from django.db import models

from game.validators import *


# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=20,
                                unique=True,
                                validators=[validate_username])

    password = models.CharField(max_length=50,
                                validators=[validate_password])

    rank = models.CharField(max_length=1,
                            choices=[("N", "Noob"), ("I", "Intermediate"), ("P", "Pro"), ("K", "King")],
                            default="N")

    email = models.EmailField(max_length=254,
                              blank=True, null=True)

    age = models.IntegerField(validators=[validate_age])

    score = models.DecimalField(max_digits=9,
                                decimal_places=3,
                                default=0,
                                validators=[validate_score])
