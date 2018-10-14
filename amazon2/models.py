from django.db import models
from cloudinary.models import CloudinaryField

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=200)
    email   = models.CharField(max_length=40)
    hashed_password = models.CharField(max_length=30)

    class Meta:
      db_table = 'user'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=60, primary_key=True)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id      = models.AutoField(primary_key=True)
    title        = models.CharField(max_length=200)
    genre        = models.ManyToManyField(Genre)
    author       = models.CharField(max_length=200)
    description  = models.CharField(max_length=2000)
    status       = models.CharField(max_length=30)
    condition    = models.CharField(max_length=30)
    cover        = CloudinaryField('image')
    release_date = models.DateTimeField()
    owner        = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
      db_table   = 'book'

    def __str__(self):
        return self.title

class Loan(models.Model):
    loan_id        = models.AutoField(primary_key=True)
    genre          = models.CharField(max_length=30)
    loan_date      = models.DateTimeField()
    retrieval_date = models.DateTimeField()
    book           = models.ForeignKey('Book', on_delete=models.CASCADE)
    client         = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
      db_table = 'loan'


class Review(models.Model):
    ŗeview_id = models.AutoField(primary_key=True)  #what?¸
    stars   = models.SmallIntegerField()
    comment = models.CharField(max_length=600)
    loan    = models.ForeignKey('Loan', on_delete=models.CASCADE)

    class Meta:
      db_table = 'review'



