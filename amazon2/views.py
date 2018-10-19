from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from amazon2.constants import StatusConstants
from .models import Book, BookOwner, Loan, Notification
import random

# Create your views here.
from django.template import loader

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    owner = BookOwner.objects.get(pk=user.pk)
    books = Book.objects.all().exclude(owner=owner).order_by('?')[:4]
    context = {'user': request.user}
    if len(books) == 4:
        context['botd'] = books[0]
        context['recomended'] = books[1]
        context['trending'] = books[2]
        context['bur'] = books[3]
        context['burThis'] = books[0].title

    return render(request, 'index.html', context)


def search(request):
    search_query = request.GET.get('q', None)
    search_param = request.GET.get('search_param', None)
    books = Book.objects.filter(Q(title__contains=search_query) | Q(author__contains=search_query))

    if search_param and search_param != 'all':
        books.filter(genre__in=[search_param])
    return render(request, 'search-results.html', {'books': books})


def description(request, id=None):
    books = Book.objects.filter(book_id=id)

    if len(books) == 0:
        return HttpResponseNotFound('<h1>Book not found</h1>')
    print(books[0].owner.first_name)
    rating = 5
    return render(request, 'description.html', {'book': books[0]})


@login_required(login_url='/accounts/login/')
def myBooks(request):
    user = request.user
    owner = BookOwner.objects.get(pk=user.pk)
    myBooks = Book.objects.filter(owner=owner)
    ratings = {1:1,2:2,3:3,4:4} #TODO trarse bien las estreallas
    return render(request, 'myBooks.html',{'myBooks':myBooks, 'ratings':ratings, 'stars':range(1,6)})


@login_required(login_url='/accounts/login/')
def myRentals(request):
    user = request.user
    client = BookOwner.objects.get(pk=user.pk)
    myRentals = Loan.objects.filter(client=client)
    ratings = {1:1,2:2,3:3,4:4} #TODO trarse bien las estreallas
    return render(request, 'myRentals.html',{'myRentals': myRentals, 'ratings':ratings, 'stars':range(1,6)})


@login_required(login_url='/accounts/login/')
def my_notifications(request):
    user = request.user
    client = BookOwner.objects.get(pk=user.pk)
    new_notifications = Notification.objects.filter(recipient=client, status=StatusConstants.NOTIFICATION_NEW)
    old_notifications = Notification.objects.filter(recipient=client, status=StatusConstants.NOTIFICATION_SEEN)
    return render(request, 'myNotifications.html', {
        'new_notifications': new_notifications, 'old_notifications': old_notifications
    })
    
def searchResults(request):
    return render(request, 'search-results.html', {})


 
  
 
 
 
 
 
 
  
 
 
