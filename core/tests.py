from django.test import TestCase
from core.models import Contact
from django.contrib.auth import get_user_model
from django.utils import timezone
from core.forms import ContactForm

User = get_user_model()

class ContactTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name='Bravin123', email='bravintester@gmail.com',
            subject='Contact Model Test', message="This is a test message",
            read=True, created=timezone.now(), updated=timezone.now(),
        )
    def test_contact_is_posted(self):
        contact = Contact.objects.get(name="Bravin123")
        self.assertEqual(contact.subject, 'Contact Model Test')
    
    def test_contactform_is_valid(self):
        form = ContactForm({
            'name': 'Brian Testing', 'email': 'brian@gmail.com',
            'subject': 'test by brian', 'message': 'Test sent by Brian',
        })
        self.assertTrue(form.is_valid())
        c1 = form.save(commit=False)
        c1.read = True
        c1.save()
        self.assertEqual(c1.name, 'Brian Testing')
        self.assertEqual(c1.message, 'Test sent by Brian')