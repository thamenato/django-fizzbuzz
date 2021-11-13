from django.urls import path
from fizzbuzz import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("fizzbuzz/", views.get_post_fizzbuzz, name="get_post_fizzbuzz"),
    path("fizzbuzz/<int:pk>/", views.get_fizzbuzz_details, name="get_fizzbuzz_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
