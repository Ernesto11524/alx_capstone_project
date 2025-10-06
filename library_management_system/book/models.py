from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

# This model is responsible for creating books
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=15)
    published_date = models.DateField()
    number_of_copies = models.IntegerField()
    number_of_copies_available = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
    

# This model is reposible for handling transactions made by users.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transactions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_transactions')
    time_of_transaction = models.DateTimeField()
    borrow_duration = models.DurationField(default=datetime.timedelta(days=14))
    check_out = models.BooleanField(default=True)
    time_of_return = models.DateTimeField()
    returned = models.BooleanField()

    def __str__(self):
        return f"{self.book} is borrowed by {self.user}"

