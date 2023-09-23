from django.urls import path
from .views import hello

urlpatterns = [
    path("blog/", hello, name="hello")
]
