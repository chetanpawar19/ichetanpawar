from django.db import models

class Highlights(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
