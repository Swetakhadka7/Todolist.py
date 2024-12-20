from django.shortcuts import render,HttpResponse, redirect
from .models import Todolist 
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
    return render(request,'contact.html')

    return HttpResponse("This is contact page")
def about(request):
    return HttpResponse("This is about page")
def welcome(request):
    return HttpResponse("This is welcome page")

def todo(request):
   tasks = Todolist.objects.all()
   total_task = tasks.count()
   total_complete = tasks.filter(status = True).count()
   total_incomplete = tasks.filter(status = False).count()
   context = {
      "tasks":tasks,
      "total_task" : total_task,
      "total_complete" : total_complete,
      "total_incomplete" : total_incomplete
   }
   return render(request,'todolist.html', context)

def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description =request.POST.get ('description')
        if title =="" and description =="":
            context = {"error":"Both fields are empty"}
            return render (request, 'create.html',context)
            # return HttpResponse("Both fileds are empty")
        Todolist.objects.create(title= title, description= description)
        return redirect("/todo")
        # return HttpResponse(description)
        return HttpResponse(title)
    return render(request,'create.html')

def update_task(request, pk):
    task = Todolist.objects.get(pk=pk)
    if request.method == "POST":
    #     # Update the task with form data
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/todo')  # Redirect only after saving the task
    
    # If not a POST request, render the form with the current task details
    context = {
        "task": task
    }
    return render(request, "update.html",context)

    
def Mark_completed(request,pk):
    task = Todolist.objects.get(pk = pk)
    task.status = True
    task.save()
    return redirect('/todo')

def Delete_task(request, pk):
    print("Delete task view called")  # Debug message
    task = Todolist.objects.get(pk=pk)
    if request.method == "POST":
        print("POST request received")  # Debug message
        task.delete()
        print("Task deleted")  # Debug message
        return redirect('/todo')

    context = {"task": task}
    return render(request, 'delete.html', context)


    