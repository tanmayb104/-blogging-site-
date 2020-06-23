from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    delete = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    user = models.CharField(max_length=100)
    