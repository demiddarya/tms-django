from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=20000)
    author = models.CharField(max_length=200)
