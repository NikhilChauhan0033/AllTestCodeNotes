from django.db import models

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='productImage/' ,null=True,blank=True)

    def __str__(self):
        return self.name
    
class StoreValue(models.Model):
    name = models.CharField(max_length=100)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.BigIntegerField()

    def __str__(self):
        return self.name