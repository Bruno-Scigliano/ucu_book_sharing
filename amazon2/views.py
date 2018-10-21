from datetime import datetime

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
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
    context = {'user': request.user, 'notifications': len(get_new_notifications(user))}
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
    return render(request, 'myBooks.html',{'myBooks':myBooks, 'ratings':ratings, 'stars':range(1,6), 'notifications': len(get_new_notifications(user)) })


@login_required(login_url='/accounts/login/')
def myRentals(request):
    user = request.user
    client = BookOwner.objects.get(pk=user.pk)
    myRentals = Loan.objects.filter(client=client, status__in=[StatusConstants.LOAN_ONGOING])
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


@login_required(login_url='/accounts/login/')
def my_notifications(request):

    user = request.user
    client = BookOwner.objects.get(pk=user.pk)
    new_notifications = Notification.objects.filter(recipient=client, status=StatusConstants.NOTIFICATION_NEW)
    old_notifications = Notification.objects.filter(recipient=client, status=StatusConstants.NOTIFICATION_SEEN)
    return render(request, 'myNotifications.html', {
        'new_notifications': new_notifications, 'old_notifications': old_notifications
    })


@login_required(login_url='/accounts/login/')
def RentBookView(request):
    message = ''
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            user = request.user
            sender = BookOwner.objects.get(pk=user.pk)
            rental_book = Book.objects.get(book_id=book_id)
            rental_book.status = StatusConstants.BOOK_LOANED
            rental_book.save()
            loan = Loan(
                status=StatusConstants.LOAN_ONGOING, client=sender, book=rental_book, loan_date=datetime.now(), retrieval_date=datetime.now()
            )
            loan.save()
            notify_message = "{} wants to read {}".format(sender.first_name, rental_book.title)
            notify = Notification(sender=sender, recipient=rental_book.owner, message=notify_message, book=rental_book)
            notify.save()
            message = 'Request Sent!'
        else:
            message = 'No book'
    return redirect('/', message=message)

@login_required(login_url='/accounts/login/')
def return_book(request):
    message = ''
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            user = request.user
            sender = BookOwner.objects.get(pk=user.pk)
            rental_book = Book.objects.get(book_id=book_id)
            rental_book.status = StatusConstants.BOOK_FREE
            rental_book.save()
            loan = Loan.objects.get(book=rental_book, status=StatusConstants.LOAN_ONGOING)
            #TODO:Cambiar a LOAN_CONFIRM_PENDING #######
            loan.status = StatusConstants.LOAN_FINISHED#
            ############################################
            retrieval_date = datetime.now()
            loan.save()
            notify_message = "{} wants to return {}".format(sender.first_name, rental_book.title)
            notify = Notification(sender=sender, recipient=rental_book.owner, message=notify_message, book=rental_book)
            notify.save()
            message = 'Request to return Sent!'
        else:
            message = 'No book'
    return redirect('/', message=message)

def get_new_notifications(user):
    client = BookOwner.objects.get(pk=user.pk)
    notifications = Notification.objects.filter(recipient=client, status=StatusConstants.NOTIFICATION_NEW)
    return notifications