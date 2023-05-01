import uuid as uuid

# Create your models here.
from django.db import models




class Url(models.Model):
    link =models.CharField(max_length=1000)
    uuid = models.CharField(max_length=5, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.link} ({self.uuid})"