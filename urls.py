

from django.http import HttpResponse
from django.urls import path
from . import views


def index(request):
    return HttpResponse("This is my first project")

urlpatterns = [
    path('', index),
    path('test', views.index),
]
