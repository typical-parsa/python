from django.shortcuts import render
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todopage/todos.html', {"todos" : todos})