from django.test import TestCase, Client
from django.urls.base import reverse
from rest_framework import status
from fizzbuzz.models import Fizzbuzz
from fizzbuzz.serializers import FizzbuzzSerializer
import json

client = Client()


class GettAllFizzbuzzTest(TestCase):
    def setUp(self):
        Fizzbuzz.objects.create(useragent="SomeAgent", message="A message!")
        Fizzbuzz.objects.create(useragent="SomeAgent", message="Another one.")
        Fizzbuzz.objects.create(useragent="SomeAgent", message="Last message")

    def test_get_all_fizzbuzz(self):
        response = client.get(reverse("get_post_fizzbuzz"))

        fizzbuzz_all = Fizzbuzz.objects.all()
        serializer = FizzbuzzSerializer(fizzbuzz_all, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetFizzbuzzDetails(TestCase):
    def setUp(self):
        self.test_fizzbuzz = Fizzbuzz.objects.create(
            useragent="SomeAgent", message="A message!"
        )

    def test_get_valid_fizzbuzz_details(self):
        response = client.get(
            reverse("get_fizzbuzz_details", kwargs={"pk": self.test_fizzbuzz.pk}),
        )
        db_fizzbuzz = Fizzbuzz.objects.get(pk=self.test_fizzbuzz.pk)
        serializer = FizzbuzzSerializer(db_fizzbuzz)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_fizzbuzz_details(self):
        response = client.get(reverse("get_fizzbuzz_details", kwargs={"pk": 123}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PostCreateFizzbuzzTest(TestCase):
    def setUp(self):
        self.valid_payload = {"message": "Lorem ipsum"}
        self.invalid_payload = {}
        self.user_agent = "TestAgent"

    def test_create_valid_fizzbuzz(self):
        response = client.post(
            reverse("get_post_fizzbuzz"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
            HTTP_USER_AGENT=self.user_agent,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_fizzbuzz(self):
        response = client.post(
            reverse("get_post_fizzbuzz"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
            HTTP_USER_AGENT=self.user_agent,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_request(self):
        """Send request without defining an User-Agent"""
        response = client.post(reverse("get_post_fizzbuzz"))
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
