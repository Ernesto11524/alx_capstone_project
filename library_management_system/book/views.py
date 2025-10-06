from django.shortcuts import render, redirect
from .forms import ModifiedUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Book, Transaction
from django.contrib.auth.models import User
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