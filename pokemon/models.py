from django.db import models

# Create your models here.

class Pokemon(models.Model):
  name = models.CharField(max_length=64)
  link = models.CharField(max_length=200)
  vote = models.IntegerField(default=0)

  def __str__(self):
    return self.name
