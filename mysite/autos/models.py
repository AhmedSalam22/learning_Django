from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text= "please enter a make" ,
        validators= [MinLengthValidator(5,"Should greater than 5")]
    )

    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        return self.nickname