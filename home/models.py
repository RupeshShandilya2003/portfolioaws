from django.db import models

# Create your models here.
class homes(models.Model):
    name = models.CharField(default="null",max_length=30)
    email = models.EmailField(default="abc@gmail.com")
    message = models.CharField(default="knkjnkjnknkn",max_length=500)

    def __str__(self):
        return self.name