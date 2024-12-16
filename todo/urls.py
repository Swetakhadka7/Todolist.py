from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home),
    path('home/',home),
    path('contact/',contact),
    path('about/',about),
    path('welcome/',welcome)
]