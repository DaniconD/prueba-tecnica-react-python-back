from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.
class Community(models.Model):
  name=models.CharField(max_length=100)
  category=models.CharField(max_length=100, blank=True)
  parent_community=models.CharField(max_length=100, blank=True)
  short_description=models.TextField()
  description=models.TextField(blank=True)