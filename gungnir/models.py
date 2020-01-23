from django.db import models

class Predict(models.Model):
    image = models.ImageField(upload_to = 'images/', height_field = None, width_field = None)
    summary = models.CharField(max_length = 200)
