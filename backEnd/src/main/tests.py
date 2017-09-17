# @Author: andreacasino
# @Date:   2017-09-14T19:03:34+01:00
# @Last modified by:   andreacasino
# @Last modified time: 2017-09-16T02:13:45+01:00

from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from main.models import Palindrome
from main.serializers import PalindromeSerializer

class modelTest(TestCase):

    def setUp(self):
        self.testPalindrome = Palindrome(text="Dammit I'm mad")
        self.testPalindrome.save()

    def test_creation(self):
        #Check if text is saved
        latestPalindromeText = Palindrome.objects.get(pk=1).text
        self.assertEqual(latestPalindromeText, "Dammit I'm mad", msg='Object cannot be created')



class serializerTest(TestCase):

    def setUp(self):
        self.testPalindrome = Palindrome(text="Noon")
        self.testPalindrome.save()
        self.serializer = PalindromeSerializer(self.testPalindrome)

    def test_serialization(self):
        self.assertEqual(self.serializer.data,{"text":"Noon"}, msg='Serialization was not possible')

    def test_deserialization(self):
        #New object
        self.testPalindrome = Palindrome(text="A man, a plan, a canal: Panama.")
        self.testPalindrome.save()
        self.serializer = PalindromeSerializer(self.testPalindrome)

        content = JSONRenderer().render(self.serializer.data)
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        self.serializer = PalindromeSerializer(data=data)

        #Check if deserialized data is valid
        self.assertTrue(self.serializer.is_valid(), msg='Serialization was not valid')
        #Check if serialized data is correct
        self.assertEqual(self.serializer.data,{"text":"A man, a plan, a canal: Panama."},
                                                msg='Serialization text error')


class APITest(TestCase):

    def setUp(self):
         self.client = APIClient()
         self.palindrome = Palindrome

    def test_get(self):
        response = self.client.get(reverse('contact'))
        #Test that get request is able to go through
        self.assertEqual(response.status_code,200,msg="Wrong status code")

    def test_post(self):
        #Check if a non palindrome outputs the correct response (false)
        data = {"text":"Not a palindrome"}
        response = self.client.post(reverse('contact'),
                                    data,
                                    format="json")

        self.assertEqual(response.content,b'false',msg="Not palindrome post found true, \
                                                    should be false")

        #Check if a blank input outputs the correct response (false)
        data = {"text":""}
        response = self.client.post(reverse('contact'),
                                    data,
                                    format="json")

        self.assertEqual(response.content,b'false',msg="Blank post found true, \
                                                    should be false")

        #Check if a whitespace input outputs the correct response (false)
        data = {"text":"   "}
        response = self.client.post(reverse('contact'),
                                    data,
                                    format="json")

        self.assertEqual(response.content,b'false',msg="Whitespace post found true, \
                                                    should be false")

        #Evaluate that palindrome is detected,along with
        #whitespace, capitalization and punctuation not affecting the evaluation
        data = {"text":"  Al lets   Della call Ed Stella.   "}
        response = self.client.post(reverse('contact'),
                                    data,
                                    format="json")

        self.assertEqual(response.content,b'true',msg="Palindrome post found false, \
                                                    should be true")
