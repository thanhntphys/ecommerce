from django.db import models

# Create your models here.



class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name