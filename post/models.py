from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class GdsModel(models.Model):
     GdsImg = models.FileField()
     title=models.CharField(max_length=20)
     description=models.TextField()
     date=models.DateTimeField(blank=True, null=True)
     class Meta:
         ordering = ['-date']
     def __str__(self):
        return self.title
