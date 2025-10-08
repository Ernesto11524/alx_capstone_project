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
    path('api/books/', book_views.ListBooks.as_view(), name='api_books'),
    path('api/create/', book_views.CreateBooks.as_view(), name='create_books'),
    path('api/retrieve/<int:pk>/', book_views.RetrieveBooks.as_view(), name='retrieve_books'),
    path('api/delete/<int:pk>/', book_views.DeleteBooks.as_view(), name='delete_books'),
    path('api/update/<int:pk>/', book_views.UpdateBooks.as_view(), name='update_books'),

]