from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name