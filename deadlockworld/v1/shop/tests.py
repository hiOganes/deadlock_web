# Standart libraries
from http import HTTPStatus

# Other libraries
from django.test import TestCase
from django.urls import reverse

# Project libraries
from v1.shop.models.shop import Shop
from v1.shop.serializers.shop import ShopSerializer


class ShopСategories(TestCase):
    fixtures = ['v1.shop.json']

    def setUp(self):
        pass
    
    def test_weapon_list(self):
        path = reverse('api:shop-weapon')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_vitality_list(self):
        path = reverse('api:shop-vitality')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_spirit_list(self):
        path = reverse('api:shop-spirit')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        
    def tearDown(self):
        pass


class ShopSearch(TestCase):
    fixtures = ['v1.shop.json']
    search_empty = '?search='
    search_not_exist = '?search=not_exist'
    search_exist = {
        'weapon': '?search=infuser', 
        'vitality': '?search=health', 
        'spirit': '?search=decay'
        }

    def setUp(self):
        pass

    def test_shop_search(self):
        path = reverse('api:shop-weapon')
        response_empty = self.client.get(path + self.search_empty)
        response_not_exist = self.client.get(path + self.search_not_exist)
        response_exist = self.client.get(path + self.search_exist['weapon'])
        self.assertFalse(response_not_exist.content.decode().rstrip('[]'))

    def tearDown(self):
        pass