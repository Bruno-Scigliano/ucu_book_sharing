from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, User
import random

# Create your views here.
from django.template import loader


def index(request):
    books = Book.objects.all()
    context = {}
    context['botd'] = books[0]
    context['recomended'] = books[1]
    context['trending'] = books[2]
    context['bur'] = books[3]
    context['burThis'] = books[0].title

    return render(request, 'index.html', context)


def description(request, id=None):
    book = Book.objects.get(book_id=id)
    rating = 5
    return render(request, 'description.html', {'book': book})

def myBooks(request):
    user = User.objects.all()[0] #TODO Traerse el usuario
    myBooks = Book.objects.filter(owner=user)
    ratings = {1:1,2:2,3:3,4:4} #TODO trarse bien las estreallas
    return render(request, 'myBooks.html',{'myBooks':myBooks, 'ratings':ratings, 'stars':range(1,6)})
