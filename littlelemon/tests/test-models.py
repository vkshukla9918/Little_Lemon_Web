from django.test import TestCase
from restaurant.models import Menu

class MenuItemTestCase(TestCase):
    def test_get_item(self):
        item = Menu(Title ='Burger', price=5.00, Inventory=10)
        self.assertEqual(item, 'Burger : 5.00')
