from django.db import models

# Create your models here.
class Farmers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    joined_date = models.DateField(null=True)
    cows_in_own = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def call_me(self):
        return {"first name": self.firstname, "": self.lastname, "":self.cows_in_own}


class Cows(models.Model):
    cow_name = models.CharField(max_length=255)
    price_for_one = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.cow_name}"
