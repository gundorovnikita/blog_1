from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=20)
     def __str__(self):
         return self.name


class GdsModel(models.Model):
     GdsCat = models.ForeignKey(Category, on_delete=models.CASCADE)
     GdsImg = models.FileField()
     title=models.CharField(max_length=20)
     description=models.TextField()
     date=models.DateTimeField(blank=True, null=True)
     class Meta:
         ordering = ['-date']
     def __str__(self):
        return self.title
