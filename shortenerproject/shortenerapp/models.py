from django.db import models


class Url(models.Model):
    link = models.URLField(max_length=255)
    uuid = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.link} ({self.uuid})"
