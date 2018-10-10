from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=40)
    hashed_password = models.CharField(max_length=30)
    class Meta:
      db_table = 'user'

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    release_date = models.DateTimeField()
    owner_id = models.ForeignKey('User', on_delete=models.CASCADE)
    class Meta:
      db_table = 'book'

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=30)
    loan_date = models.DateTimeField()
    retrieval_date = models.DateTimeField()
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    client_id = models.ForeignKey('User', on_delete=models.CASCADE)
    class Meta:
      db_table = 'loan'

class Review(models.Model):
    loan_id = models.AutoField(primary_key=True)
    stars = models.SmallIntegerField()
    comment = models.CharField(max_length=150)
    loan_id = models.ForeignKey('Loan', on_delete=models.CASCADE)
    class Meta:
      db_table = 'review'
