from django.db import models

# Create your models here.

class Calculation(models.Model):
    name = models.CharField(max_length=100)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    total = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name