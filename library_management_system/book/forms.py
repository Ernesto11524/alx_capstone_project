from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book, Transaction


# This is a class designed to include other relevant fields like firstname, lastname
# in the user creation form.
class ModifiedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


# This is a form class which handles the registration of books in the database.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


# This is a form class which handles the book transactions, i.e. borrowed books in the system.
class TransactionForm(forms.ModelForm):
    time_of_return = forms.DateTimeField(required=False)
    returned = forms.BooleanField(required=False)

    class Meta:
        model = Transaction
        fields = ['user', 'book', 'borrow_duration', 'check_out', 'time_of_return', 'returned']