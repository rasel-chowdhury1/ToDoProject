from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import ToDo
# Create your views here.

def home(request):
    context = {
        'todo_list' : ToDo.objects.all()
    }
    return render(request,'todo/index.html',context)

def insert_todo_item(request):
    todo = ToDo(content = request.POST['content'])
    todo.save()
    return redirect('/home/')

def delete_todo_item(request,todo_id):
    todo_to_delete = ToDo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/home/')