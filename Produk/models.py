from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class KeranjangBelanja(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} - {self.Product.nama_Product}'