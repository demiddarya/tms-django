from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category_id = models.IntegerField(unique=True)


class Category(models.Model):
    id = models.ForeignKey(Product, related_name='categories', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
