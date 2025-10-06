# library_management_system

# Library Management System (Django)

This project is a **Library Management System** built using Django and Django Rest Framework.  
It is designed to manage library resources, handle book borrowing activities, and organize user access for both administrators and regular users.  
The project also serves as a practical learning experience for understanding Django’s authentication system, models, views, and templates.

---

## Features Implemented So Far

- **User Authentication**
    - Uses Django’s built-in authentication system for login, logout, and registration.
    - Two types of users:
        - **Admin Users** – can manage books, view borrowing records, and oversee the system.
        - **Normal Users** – can view available books, borrow books, and view their borrowing history.
    - Custom login and registration pages integrated with Django messages for user feedback.

- **Book Management**
    - Admins can add, update, or delete books from the system.
    - Each book record includes:
        - Title  
        - Author  
        - ISBN  
        - Publication date  
        - Availability status  
    - Books are displayed dynamically on both admin and user dashboards.

- **Borrowing System**
    - Normal users can borrow available books.
    - Borrowed books are linked to the user who borrowed them.
    - Each borrowing record includes:
        - Borrow date  
        - Return due date  
        - Returned status (Yes/No)
    - Automatic checks ensure that unavailable books cannot be borrowed again until returned.

- **Admin Dashboard**
    - Displays system statistics such as:
        - Total number of books  
        - Books currently borrowed  
        - Active users  
        - Recently added books
    - Provides quick access to manage library items and monitor borrowing activity.

- **User Dashboard**
    - Displays:
        - List of books available for borrowing  
        - User’s borrowing history  
        - Notifications about borrowed or overdue books
    - Clean and responsive design for better user experience.

- **Frontend Integration**
    - Uses Django templates and static files for UI rendering.
    - Includes consistent base layout with navigation and message display.
    - CSS designed for clear visual separation between admin and user interfaces.

- **Logout Functionality**
    - Implemented using Django’s built-in `LogoutView`.
    - Clears user sessions and redirects to the login page with a logout success message.

---

## Future Enhancements

- Add book search and filtering by title, author, or category.  
- Implement overdue book notifications via email.  
- Add REST API endpoints for mobile or external access.  
- Enable book reservations and renewal requests.  
- Include user profile management with borrowing limits and history tracking.
