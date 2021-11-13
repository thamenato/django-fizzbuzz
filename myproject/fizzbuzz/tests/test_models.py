import datetime

from django.test import TestCase
from fizzbuzz.models import Fizzbuzz


class FizzbuzzTest(TestCase):
    """Test module for Fizzbuzz model"""

    def setUp(self):
        Fizzbuzz.objects.create(useragent="Agent1", message="Cool message!")
        Fizzbuzz.objects.create(useragent="Agent2", message="Another message.")

    def test_fizzbuzz(self):
        fizzbuzz_one = Fizzbuzz.objects.get(pk=1)
        fizzbuzz_two = Fizzbuzz.objects.get(pk=2)

        self.assertEqual(fizzbuzz_one.message, "Cool message!")
        self.assertEqual(fizzbuzz_two.message, "Another message.")

        self.assertIsInstance(fizzbuzz_one.creation_date, datetime.datetime)
