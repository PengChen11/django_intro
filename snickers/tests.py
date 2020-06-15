from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnickersTests(SimpleTestCase):

    def helper_status_200(self,url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    def helper_template_used(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, url_name+'.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_status(self):
        self.helper_status_200('home')

    def test_home_page_template(self):
        self.helper_template_used('home')

    def test_about_page_status(self):
        self.helper_status_200('about')

    def test_about_page_template(self):
        self.helper_template_used('about')
