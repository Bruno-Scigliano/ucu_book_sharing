from django.contrib import admin
from .models import User, Genre, Book, Loan, Review
# Register your models here.
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Review)

