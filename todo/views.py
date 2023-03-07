from django.shortcuts import render
from .models import Todo


def todo_list(request):
    todos = Todo.objects.order_by('-created_date')
    return render(request, 'todo/todo_list.html', {'todos': todos})
