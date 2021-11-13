from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from fizzbuzz.models import Fizzbuzz
from fizzbuzz.serializers import FizzbuzzSerializer


class FizzbuzzList(APIView):
    def get(self, request, format=None):
        fizzbuzz_all = Fizzbuzz.objects.all()
        serializer = FizzbuzzSerializer(fizzbuzz_all, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        raw_data = request.data
        raw_data["useragent"] = request.META["HTTP_USER_AGENT"]

        serializer = FizzbuzzSerializer(data=raw_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FizzbuzzGetDetails(generics.RetrieveAPIView):
    queryset = Fizzbuzz.objects.all()
    serializer_class = FizzbuzzSerializer
