from django.contrib import admin
from .models import BookOwner, Genre, Book, Loan, Review, Notification
# Register your models here.
admin.site.register(BookOwner)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Review)
admin.site.register(Notification)

