from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','status']
    list_filter =['status']
    search_fields = ['title']
    list_per_page = 5


