from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from fizzbuzz import views

urlpatterns = [
    path("fizzbuzz/", views.FizzbuzzList.as_view()),
    path("fizzbuzz/<int:pk>/", views.FizzbuzzGetDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
