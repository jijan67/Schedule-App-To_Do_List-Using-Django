from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import TodoList

def index(request):
    """
    View to handle the display and submission of the to-do list.
    """
    item_list = TodoList.objects.order_by("-date")
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully!")
            return redirect('todo')
    else:
        form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST Schedule Made by Jijan",
    }
    return render(request, 'index.html', page)

def remove(request, item_id):
    """
    View to handle the removal of a to-do item.
    """
    item = get_object_or_404(TodoList, id=item_id)
    item.delete()
    messages.info(request, "Item removed successfully!")
    return redirect('todo')

def update(request, item_id):
    """
    View to handle the updating of a to-do item.
    """
    item = get_object_or_404(TodoList, id=item_id)
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully!")
            return redirect('todo')
    else:
        form = TodoForm(instance=item)

    page = {
        "forms": form,
        "title": "Update TODO Item",
        "item_id": item_id,
    }
    return render(request, 'update.html', page)
