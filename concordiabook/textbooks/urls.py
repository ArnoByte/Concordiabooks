from django.urls import path
from .views import textbook_list

urlpatterns = [
    path("textbooks/<str:course_code>/", textbook_list, name="textbook_list"),
]