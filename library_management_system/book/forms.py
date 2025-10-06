from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# This is a class designed to include other relevant fields like firstname, lastname
# in the user creation form.
class ModifiedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']