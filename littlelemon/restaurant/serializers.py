from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'price','Inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['Name', 'No_of_guests','BookingDate']
