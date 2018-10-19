from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from amazon2.constants import StatusConstants
from .models import Book, BookOwner, Loan, Notification
import random

# Create your views here.
from django.template import loader


@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    owner = BookOwner.objects.get(pk=user.pk)
    books = Book.objects.filter(owner=owner)
    context = {'user': request.user}
    # context['botd'] = books[0]
    # context['recomended'] = books[1]
    # context['trending'] = books[2]
    # context['bur'] = books[3]
    # context['burThis'] = books[0].title

    return render(request, 'index.html', context)


def description(request, id=None):
    book = Book.objects.get(book_id=id)
    rating = 5
    return render(request, 'description.html', {'book': book})


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


 
  
 
 
 
 
 
 
  
 
 