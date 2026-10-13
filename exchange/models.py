from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True, default="")
    languages = models.CharField(max_length=200)
    places = models.PositiveIntegerField()
    places_is_limit = models.BooleanField(default=False)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()