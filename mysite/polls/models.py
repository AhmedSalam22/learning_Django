from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)

    def __str__(self):
        return "{}".format(self.name)