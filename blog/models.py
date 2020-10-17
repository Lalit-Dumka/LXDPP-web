from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    author = models.CharField(max_length=200)
    language = models.CharField(max_length=101)
    category = models.CharField(max_length=200)
    readtime = models.IntegerField()
