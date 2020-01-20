from django.db import models

# Create your models here.
class Visualize(models.Model):
    bidytext = models.TextField()
    vcompanyname = models.CharField(max_length = 100)
    sdate = models.CharField(max_length = 100)
    edate = models.CharField(max_length = 100)
