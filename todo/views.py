from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def say_hi2(request):
    return HttpResponse("hello world 2 !")


def say_hitop(request):
    return HttpResponse("hello world from the top !")


def say_hi(request):
    return HttpResponse("hello world !")


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, 'todo/add_item.html', context)


def say_todo(request):
    return render(request, 'todo/todo.html')
