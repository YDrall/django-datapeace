from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from rest_framework import status

from users.models import User

client = Client()


class SimpleUserListTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create(first_name='Test1', last_name='Test1 last',
                            company_name='Company 1', age=25, city='Delhi', state='Delhi',
                            zip='110041', email='test@gmail.com', web='https://web.com')
        User.objects.create(first_name='Test2', last_name='Test2 last',
                            company_name='Company 1', age=15, city='Delhi', state='Delhi',
                            zip='110006', email='test900@gmail.com', web='https://web.com')
        User.objects.create(first_name='Test4', last_name='Test4 last',
                            company_name='Company 2', age=18, city='Delhi', state='Delhi',
                            zip='110001', email='test007@gmail.com', web='https://web.com')
        User.objects.create(first_name='Test5', last_name='Test5 last',
                            company_name='Company 1', age=20, city='Delhi', state='Delhi',
                            zip='110041', email='test@gmail.com', web='https://web.com')
        User.objects.create(first_name='Test6', last_name='Test6 last',
                            company_name='D Company 1', age=19, city='Delhi', state='Delhi',
                            zip='110041', email='test@gmail.com', web='https://web.com')
        User.objects.create(first_name='Test8', last_name='Test8 last',
                            company_name='B Company 10', age=40, city='Delhi', state='Delhi',
                            zip='110041', email='test@gmail.com', web='https://web.com')

    def test_get_all_user_default_page_size(self):
        response = client.get(reverse('user_list_create_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 5)
        self.assertEqual(response.data.get('count'), 6)

    def test_list_pagination_limit(self):
        response = client.get(reverse('user_list_create_api'), data={'limit': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 6)
        self.assertEqual(len(response.data.get('results')), 2)

    def test_list_pagination_page_number(self):
        response = client.get(reverse('user_list_create_api'), data={'limit': 2, 'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 6)
        self.assertEqual(len(response.data.get('results')), 2)

        response = client.get(reverse('user_list_create_api'), data={'page': 3})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_name_search_filter(self):
        response = client.get(reverse('user_list_create_api'), data={'name': 'teSt'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 5)

        response = client.get(reverse('user_list_create_api'), data={'name': 'JJ'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 0)

        response = client.get(reverse('user_list_create_api'), data={'name': 'sT1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 1)

        response = client.get(reverse('user_list_create_api'), data={'name': 'sT'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 5)

        response = client.get(reverse('user_list_create_api'), data={'name': 'last'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 5)

        response = client.get(reverse('user_list_create_api'), data={'name': '1 last'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 1)

    def test_sort_filter(self):
        response = client.get(reverse('user_list_create_api'), data={'sort': 'first_name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('results')[0].get('first_name'), 'Test1')

        response = client.get(reverse('user_list_create_api'), data={'sort': '-first_name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('results')[0].get('first_name'), 'Test8')

        response = client.get(reverse('user_list_create_api'), data={'sort': '-age'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('results')[0].get('age'), 40)
