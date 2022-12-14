from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class DiagonaleApiTest(APITestCase):
    def test_diagonale_1(self):
        size = 15
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'size': size})
        result = response.data['diagonal'].strip().split(' ')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), size-1)

    def test_diagonale_2(self):
        size = 10
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'size': size})
        result = response.data['diagonal'].strip().split(' ')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), size-1)

    def test_diagonale_3(self):
        size = 20
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'size': size})
        result = response.data['diagonal'].strip().split(' ')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), size-1)

    def test_response_invalid_size_1(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'size': 'ilegtyv'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_response_invalid_size_2(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'size': 12.25})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_response_invalid_size_3(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'size': '12.25'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)