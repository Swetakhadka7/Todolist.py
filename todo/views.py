from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    person =[
    {"name": "Alice", "age": 15},
    {"name": "Bob", "age": 12},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 27},
    {"name": "Ethan", "age": 29},
    {"name": "Fiona", "age": 24},
    {"name": "George", "age": 26},
    {"name": "Hannah", "age": 28},
    {"name": "Ian", "age": 55},
    {"name": "Julia", "age": 31},
]

    context = {
        "name":"sweta",
        "persons":person
    }
    return render(request,'index.html',context)
    # return HttpResponse("Hello World")

def contact(request):
    return HttpResponse("This is contact page")
def about(request):
    return HttpResponse("This is about page")
def welcome(request):
    return HttpResponse("This is welcome page")