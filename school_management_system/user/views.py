from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})