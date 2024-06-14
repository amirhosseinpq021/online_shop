from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpAndLoginPageTest(TestCase):

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            'amirhossein',
            'amir@gmail.com',
        )
        self.assertEqual(get_user_model().objects.all().count(), 1),
        self.assertEqual(get_user_model().objects.all()[0].username, 'amirhossein'),
        self.assertEqual(get_user_model().objects.all()[0].email, 'amir@gmail.com'),
