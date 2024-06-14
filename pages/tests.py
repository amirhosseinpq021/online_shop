from django.test import TestCase

from django.contrib.auth.models import User

from django.shortcuts import reverse


class OnlineShopTest(TestCase):

    # تست این که بر اساس یو ار ال چک کنه صفحه میاره یا نه
    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # تست بر اساس name در urls
    def test_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # تست بر اساس name در urls
    def test_aboutus_url_by_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    # تست اینکه عنوان پست در صفحه باشد
    def test_title_on_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'home page')

    # تست اینکه عنوان پست در صفحه باشد
    def test_title_on_aboutus_page(self):
        response = self.client.get(reverse('about_us'))
        self.assertContains(response, 'aboutus')

    # ببینیم تمپلیت رندر میشه یا نه
    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # ببینیم تمپلیت رندر میشه یا نه
    def test_aboutus_template_used(self):
        response = self.client.get(reverse('about_us'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')
