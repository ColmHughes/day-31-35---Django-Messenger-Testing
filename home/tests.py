from django.test import TestCase
from .views import show_home
from django.core.urlresolvers import resolve
# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, show_home)