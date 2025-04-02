from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Burger = Menu.objects.create(dish='Burger', price=70, inventory=10)
        Pizza = Menu.objects.create(dish='Pizza', price=300, inventory=20)
    
    def test_getall(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Burger')
        self.assertContains(response, 'Pizza')