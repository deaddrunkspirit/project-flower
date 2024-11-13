from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=255, default='Отсутствует')
    material = models.CharField(max_length=255, default='Отсутствует')
    weight = models.FloatField(default=1)
    diameter = models.IntegerField(default=1)
    thickness = models.IntegerField(default=1)
    length = models.IntegerField(default=1)
    price = models.IntegerField(default=52)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
