from django.db import models

# Create your models here.
class Farmer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    cows_in_own = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


    def call_me(self):
        return {
            "First name:": self.firstname,
            "Last_name:": self.lastname,
            "Cows in own:":self.cows_in_own}



class Cow(models.Model):
    cow_name = models.CharField(max_length=255)
    price_for_one = models.IntegerField(null=True)
    

    def __str__(self):
        return f"{self.cow_name}"
