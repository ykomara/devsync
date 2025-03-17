from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100, unique=True)
    email=models.EmailField(unique=True)
    is_staff=models.BooleanField(default=False)

    def __str__(self):
        return self.username



