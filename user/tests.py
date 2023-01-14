from django.test import TestCase, Client
from django.urls import reverse
from .models import UserPatient
from django.forms.utils import ErrorList
# Create your tests here
class RegerstarionTest(TestCase):
    def test_regerstarion(self):
        data1={
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'qaz123qaz',
            'password2': 'qaz123qaz',
            'first_name': 'test',
            'last_name': 'test',
            'id_number': '123456789',
            'phone_number': '0512345678'
        }
        response = self.client.post(reverse('register'),data=data1,follow=True)
        # usr = UserPatient.objects.get(user_patient__username='test')
        self.assertEqual(response.status_code,200)
    def test_regerstarion_phoneLengthNotValid(self):

        data1={
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'qaz123qaz',
            'password2': 'qaz123qaz',
            'first_name': 'test',
            'last_name': 'test',
            'id_number': '123456789',
            'phone_number': '10'
        }
        response = self.client.post(reverse('register'),data=data1,follow=True)
        form  = response.context['profile_form']
        self.assertTrue('Invalid id number[id number must contain 9 digits]' in form.errors.as_text(),"[LengthNotValid]id number must contain 9 digits")
    def test_regerstarion_phoneDigitsNotValid(self):

        data1={
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'qaz123qaz',
            'password2': 'qaz123qaz',
            'first_name': 'test',
            'last_name': 'test',
            'id_number': '123456789',
            'phone_number': '12ab67890'
        }
        response = self.client.post(reverse('register'),data=data1,follow=True)
        form  = response.context['profile_form']
        self.assertTrue('Invalid id number[only numbers are allowed]' in form.errors.as_text(),"[DigitsNotValid]only numbers are allowed")


    def test_regerstarion_phoneFormatNotValid(self):

        data1={
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'qaz123qaz',
            'password2': 'qaz123qaz',
            'first_name': 'test',
            'last_name': 'test',
            'id_number': '123456789',
            'phone_number': '1234567890'
        }
        response = self.client.post(reverse('register'),data=data1,follow=True)
        form  = response.context['profile_form']
        self.assertTrue('Invalid phone number[phone number must be 10 digits]' in form.errors.as_text(),"[FormatNotValid]phone number must be 10 digits")
    # def test_regerstarion_EmailFormatNotValid(self):

    #     data1={
    #         'username': 'test',
    #         'email': 'test.test.com',
    #         'password1': 'qaz123qaz',
    #         'password2': 'qaz123qaz',
    #         'first_name': 'test',
    #         'last_name': 'test',
    #         'id_number': '123456789',
    #         'phone_number': '1234567890'
    #     }
    #     response = self.client.post(reverse('register'),data=data1,follow=True)
    #     form  = response.context['profile_form']
    #     self.assertTrue('Invalid phone number[phone number must be 10 digits]' in form.errors.as_text(),"[FormatNotValid]phone number must be 10 digits")
        


        
