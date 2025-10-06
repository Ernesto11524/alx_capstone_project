from django.shortcuts import render, redirect
from .forms import ModifiedUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
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
def admin_home(request):
    return render(request, 'book/admin_home.html')


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