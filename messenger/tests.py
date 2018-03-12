from django.test import TestCase
from .views import *
from django.core.urlresolvers import resolve

# Create your tests here.

class MessengerTests(TestCase):
    def test_inbox_resolves(self):
        home_page = resolve('/messenger/inbox/')
        self.assertEqual(home_page.func, inbox)
        
    def test_sent_resolves(self):
        home_page = resolve('/messenger/sent/')
        self.assertEqual(home_page.func, sent)
        
    def test_message_resolves(self):
        home_page = resolve('/messenger/message/1')
        self.assertEqual(home_page.func, message)
        
    def test_compose_resolves(self):
        home_page = resolve('/messenger/message/compose/')
        self.assertEqual(home_page.func, compose_message)
        
    def test_message_requires_id(self):
        response = self.client.get('/messenger/message/')
        self.assertEqual(response.status_code, 404)
        
        
    def test_index_template_is_correct(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/base.html')
        self.assertTemplateUsed(response, 'home/index.html')
        
        
        
        