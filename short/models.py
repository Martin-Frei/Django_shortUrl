from django.db import models

# Create your models here.

class shortUrl(models.Model):
    longUrl = models.URLField(max_length=300)
    shortUrlField = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return super().__str__()