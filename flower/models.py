from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    value = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
