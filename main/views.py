from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def homepage(request):
    return render(request, "index.html", "book.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")


def third(request):
    return HttpResponse("This is test page 3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)    
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    if todo.is_favorite:
            todo.is_favorite = False
    else:
        toto.is_favorite =True
        tot.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def delete_book(request, id):
    book = BookStore.objects.get(id=id)
    book.delete()

    return redirect(bookStore)

def favorite_book(request, id):
    book = BookStore.objects.get(id=id)
    if book.is_favorite:
        book.is_favorite =False
    else:
        book.is_favorite =True
        book.save()
        return redirect(bookStore)


def book_info(request, id):
    book = BookStore.objects.get(id=id)
    return render(request, 'book-detail.html', {'book': book})






