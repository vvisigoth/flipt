from django.db import models

# Create your models here.


class Module(models.Model):
  title = models.CharField(max_length=300)
  slug = models.SlugField()
