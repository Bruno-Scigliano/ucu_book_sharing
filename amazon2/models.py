from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from amazon2.constants import StatusConstants, ConditionConstants


class BookOwner(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=60, primary_key=True)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_CHOICES = (
        (StatusConstants.BOOK_FREE, StatusConstants.BOOK_FREE),
        (StatusConstants.BOOK_LOANED, StatusConstants.BOOK_LOANED)
    )
    CONDITION_CHOICES = (
        (ConditionConstants.BOOK_NEW, ConditionConstants.BOOK_NEW),
        (ConditionConstants.BOOK_USED, ConditionConstants.BOOK_USED),
        (ConditionConstants.BOOK_DAMAGED, ConditionConstants.BOOK_DAMAGED)
    )

    book_id      = models.AutoField(primary_key=True)
    title        = models.CharField(max_length=200)
    genre        = models.ManyToManyField(Genre, related_name="genre")
    author       = models.CharField(max_length=200)
    description  = models.CharField(max_length=2000)
    status       = models.CharField(max_length=30, choices=STATUS_CHOICES)
    condition    = models.CharField(max_length=30, choices=CONDITION_CHOICES)
    cover        = CloudinaryField('image', blank=True)
    release_date = models.DateTimeField()
    owner        = models.ForeignKey('BookOwner', on_delete=models.CASCADE)

    class Meta:
      db_table   = 'book'

    def __str__(self):
        return self.title


class Loan(models.Model):
    loan_id        = models.AutoField(primary_key=True)
    status         = models.CharField(max_length=30)
    loan_date      = models.DateTimeField()
    retrieval_date = models.DateTimeField()
    book           = models.ForeignKey('Book', on_delete=models.CASCADE)
    client         = models.ForeignKey('BookOwner', on_delete=models.CASCADE)

    class Meta:
      db_table = 'loan'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)  #what?¸
    stars   = models.SmallIntegerField()
    comment = models.CharField(max_length=600)
    loan    = models.ForeignKey('Loan', on_delete=models.CASCADE)

    class Meta:
      db_table = 'review'


class Notification(models.Model):
    STATUS_CHOICES = (
        (StatusConstants.NOTIFICATION_NEW, StatusConstants.NOTIFICATION_NEW),
        (StatusConstants.NOTIFICATION_SEEN, StatusConstants.NOTIFICATION_SEEN)
    )

    sender = models.ForeignKey('BookOwner', on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey('BookOwner', on_delete=models.CASCADE, related_name='recipient')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=StatusConstants.NOTIFICATION_NEW)
    message = models.CharField(max_length=600)
    book = models.ForeignKey('Book', blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
      db_table = 'notifications'
