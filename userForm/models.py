from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        email = self.email