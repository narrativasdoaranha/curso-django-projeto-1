from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes),
    path('recipes/<int:id>/', views.recipes_view),
]