from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request, 'todopage/todos.html', {"todos" : todos})

def create_todo(request):
    if request.method != "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')

        Todo.objects.create(
            author = 0,
            title = title,
            description = description,
            category = category,
            competed = False
        )
        return redirect('todo-list')
    
    return render(request, 'todo/createtodo.html')
