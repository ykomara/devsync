from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from .models import User

class TestUser(APITestCase):
    url=reverse_lazy('users-list')

    def test_list(self):
        user1= User.objects.create(email='test1@gmail.com', full_name='Mahomet', is_staff=True)
        user2= User.objects.create(email='test2@gmail.com', full_name='Oumar', is_staff=False)

        response=self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        expected=[
            {
                'id': user1.id,
                'full_name': user1.full_name,
                'email': user1.email,
                'is_staff': user1.is_staff,
            },
            {
                'id': user2.id,
                'full_name': user2.full_name,
                'email': user2.email,
                'is_staff': user2.is_staff,
            }
        ]

        self.assertEqual(response.json(), expected)

    def test_create(self):
        self.assertFalse(User.objects.exists())
        reponse=self.client.post(self.url, data={'full_name':'Leo MESSI',
                                                 'email':'lmessi@gmail.com',
                                                 'password':'leomessi10'
                                                 })
        self.assertEqual(reponse.status_code, 201)
        self.assertTrue(User.objects.exists())





