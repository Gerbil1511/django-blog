from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'glb24',
            'email': 'test@test.com',
            'message': 'Test message'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    
    def test_name_is_required(self):
        """ Test for 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Test message'
        })
        self.assertFalse(form.is_valid(), msg="Name was not provided, but form is valid"
        ) 

    def test_email_is_required(self):
        """ Test for 'email' field"""
        form = CollaborateForm({
            'name': 'glb24',
            'email': '',
            'message': 'Test message'
        })
        self.assertFalse(form.is_valid(), msg="Email was not provided, but form is valid"
        )

    def test_message_is_required(self):
        """ Test for 'message' field"""
        form = CollaborateForm({
            'name': 'glb24',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message was not provided, but form is valid"
        )

# as the the assert statement contains False, the test will pass if the form is not valid
# to get the message displaying set the assert statement to True