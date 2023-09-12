from django.db import models

# Create your models here.
"""class products(models.Model):
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.product_name"""
    

class UserInput(models.Model):
    input_field = models.CharField(max_length=255)   
    input_field1 = models.IntegerField()

    def __str__(self) -> str:
        return self.input_field,self.input_field1 