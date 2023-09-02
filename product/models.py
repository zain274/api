from django.db import models

# Create your models here.


class Product(models.Model):
    category =models.CharField(max_length=100)
    description =models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    manufactor= models.CharField(max_length=100)
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    def __str__(self):
        return self.name
