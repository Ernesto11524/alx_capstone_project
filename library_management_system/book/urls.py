from django.urls import path
from . import views as book_views

urlpatterns = [
    path('register/', book_views.register, name='register'),
    path('login/', book_views.CustomLoginView.as_view(template_name = 'book/login.html'), name='login'),
    path('logout/', book_views.custom_logout, name='logout'),
    path('admin_home/', book_views.admin_home, name='admin_home'),
    path('user_home/', book_views.user_home, name='user_home'),
    path('manage_books/', book_views.manage_books, name='manage_books'),
    path('manage_users/', book_views.manage_users, name='manage_users'),
    path('borrow_records/', book_views.borrow_records, name='borrow_records'),
]