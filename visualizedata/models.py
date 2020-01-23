from django.db import models

class VisualizeData(models.Model):
    caseContent = models.TextField()
    caseImage = models.ImageField(upload_to = 'images/')
