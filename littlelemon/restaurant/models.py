from django.db import models

# Create your models here.
class Menu(models.Model):
    ID = models.IntegerField()
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField()

class Booking(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()