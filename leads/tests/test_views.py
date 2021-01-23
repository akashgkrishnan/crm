from django.http import response
from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):
    
    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
    
    def test_check_templatename(self):
        response = self.client.get(reverse('landing-page'))
        self.assertTemplateUsed(response, 'landing.html')