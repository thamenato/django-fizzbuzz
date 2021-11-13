from fizzbuzz.models import Fizzbuzz
from rest_framework import serializers


class FizzbuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fizzbuzz
        fields = "__all__"
        read_only_fields = ["fizzbuzz_id", "creation_date"]
