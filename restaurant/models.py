from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(null=True, blank=True)
    booking_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    inventory = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title