from fizzbuzz.models import Fizzbuzz
from fizzbuzz.serializers import FizzbuzzSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def get_post_fizzbuzz(request):
    # get all fizzbuzz
    if request.method == "GET":
        fizzbuzz_all = Fizzbuzz.objects.all()
        serializer = FizzbuzzSerializer(fizzbuzz_all, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        raw_data = request.data
        try:
            raw_data["useragent"] = request.META["HTTP_USER_AGENT"]
        except KeyError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = FizzbuzzSerializer(data=raw_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_fizzbuzz_details(request, pk):
    try:
        fizzbuzz = Fizzbuzz.objects.get(pk=pk)
    except Fizzbuzz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FizzbuzzSerializer(fizzbuzz)
        return Response(serializer.data)
