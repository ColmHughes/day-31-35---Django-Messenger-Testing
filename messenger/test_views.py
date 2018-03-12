from django.test import TestCase
from .views import *
from .models import Message
from django.contrib.auth.models import User


class MessengerTests(TestCase):
    def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, 'messenger/inbox.html')
        
    def test_sent_template(self):
        response = self.client.get('/messenger/sent/')
        self.assertTemplateUsed(response, 'messenger/sent.html')
        
    def test_message_does_not_exist(self):
        response = self.client.get('/messenger/message/1')
        self.assertEqual(response.status_code, 404)
        
    def test_view_message_that_exists(self):
        sender = User(username="sender")
        sender.save()
    
    
    
    
        recipient = User(username="receiver")
        recipient.save()
    
        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()
    
        response = self.client.get('/messenger/message/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messenger/message.html")
        
        
    def test_post_message(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')
        self.client.login(username="sender", password="sender")
        
        message = {
            "subject": "Test Subject",
            "body": "Test Body",
            "recipient": recipient.id
        }

        response = self.client.post('/messenger/message/compose/', message)
        self.assertEqual(response.status_code, 302)    
        
        