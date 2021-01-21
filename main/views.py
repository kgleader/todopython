from django.shortcuts import render, HttpResponse
from .models import ToDo, BookStore


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")


def third(request):
    return HttpResponse("This is test page 3")


def bookStore(request):
    book_list = BookStore.objects.all()
    return render(request, 'books.html', {"book_list": book_list})
    