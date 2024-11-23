from django.urls import path
from django.http import HttpResponse
from home.views import home
from home import views

urlpatterns = [
    path('', home),
]