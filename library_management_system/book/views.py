from django.shortcuts import render, redirect
from .forms import ModifiedUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Book, Transaction
from django.contrib.auth.models import User
from .forms import BookForm, TransactionForm
from django.utils import timezone
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer, TransactionSerializer
from .permission import StaffOnlyMixin
# Create your views here.

# This is the registration view.
def register(request):
    if request.method == 'POST':
        form = ModifiedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has successfully been created! ')
            return redirect('login')

    else:
        form = ModifiedUserCreationForm()

    return render(request, 'book/register.html', {'form': form})


# This is the home view for admin users.
@login_required
@staff_member_required
def admin_home(request):
    # This queries all the books in the database.
    total_books = Book.objects.all() 
    # This queries all the users in the database.
    total_users = User.objects.all()
    # This queries all the transactions in the database.
    total_transactions = Transaction.objects.all()
    # This variable stores the total number of books.
    book_count  = 0
    # This variable stores the total number of users.
    user_count = 0
    # This variable store the total number of books borrowed.
    books_borrowed_count = 0
    # This variable store the total number of books which has not been returned.
    pending_return_count = 0

    # This loop count the total number of books and updates the book_count variable.
    for book in total_books:
        book_count += 1

    # This loop count the total number of users and updates the user_count variable.
    for user in total_users:
        user_count += 1

    # This loop count the total number of book transactions and updates the books_borrowed_count variable.
    for transaction in total_transactions:
        books_borrowed_count += 1

    # This loop count the total number of transactions and updates the pending_return_count variable.
    for transaction in total_transactions:
        if not transaction.returned:
            pending_return_count += 1

    context = {
        'total_books_count': book_count,
        'total_users_count': user_count,
        'total_borrowed_books_count': books_borrowed_count,
        'total_pending_return': pending_return_count,
    }

    return render(request, 'book/admin_home.html', context)

# This is the home view for normal users.
@login_required
def user_home(request):
    return render(request, 'book/user_home.html')

# This view handles user logout.
def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

# This is a class view which inherits from the built in
# login view which handles the login of a user
class CustomLoginView(LoginView):
    template_name = 'book/login.html'


    # This method makes sure the home page the user is taken to depending on the 
    # status of the user.
    def get_success_url(self):
        user = self.request.user

        if user.is_staff:
            return reverse('admin_home')
        return reverse('user_home')
    

# This view is reponsible for handling the management of books. It allows admins to register new books in the 
# database.
@staff_member_required
def manage_books(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            book_name = book_form.cleaned_data.get('title')
            messages.success(request, f"{book_name} has been saved successfully!")
            return redirect('manage_books')
    else:
        book_form = BookForm()

    return render(request, 'book/manage_books.html', {'form': book_form})

# This view also manages users. It allow admins to register new users in the database.
@staff_member_required
def manage_users(request):

    return render(request, 'book/manage_users.html')

# This view handles the history of books borrowed in the library whether returned or not.
@staff_member_required
def borrow_records(request):
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            user = request.user
            transaction.time_of_transaction = timezone.now()
            transaction.save()
            book = transaction_form.cleaned_data.get('book')
            messages.success(request, f"{book} has been successfully been borrowed by {user}!")
            return redirect('borrow_records')
        else:
            messages.error(request, "There was an error processing your form.")

    else:
            transaction_form = TransactionForm()

    return render(request, 'book/borrow_records.html', {'form': transaction_form })


class ListBooks(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    filterset_fields =['title', 'author', 'ISBN']
    search_fields = ['title', 'author', 'ISBN']
    ordering_fields = ['title', 'published_date']

class CreateBooks(StaffOnlyMixin, generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class RetrieveBooks(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UpdateBooks(StaffOnlyMixin, generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBooks(StaffOnlyMixin, generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

