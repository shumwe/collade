from django.urls import path
from core import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
