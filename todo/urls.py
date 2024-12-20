from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home),
    # path('home/',home),
    path('contact/',contact),
    # path('about/',about),
    # path('welcome/',welcome),
    path('todo/', todo),
    path('todo/create',todo_create),
    path('todo/<pk>',Mark_completed),
    path('todo/<pk>/update', update_task),
    path('todo/<pk>/delete',Delete_task),
]