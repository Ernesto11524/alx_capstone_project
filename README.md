# Library Management System (Django)

This project is a **Library Management System** built using Django and Django Rest Framework.  
It is designed to manage library resources, handle book borrowing and return activities, and organize user access for both administrators and regular users.  
The project also serves as a practical learning experience for understanding Django’s authentication system, models, views, serializers, and API development.

---

## Features Implemented So Far

### **User Authentication**
- Uses Django’s built-in authentication system for login, logout, and registration.
- Two types of users:
  - **Admin Users** – can manage books, view borrowing and return records, and oversee the system.
  - **Normal Users** – can view available books, borrow books, return borrowed books, and view their borrowing history.
- Custom login and registration pages integrated with Django messages for user feedback.

---

### **Book Management**
- Admins can add, update, or delete books from the system.
- Each book record includes:
  - Title  
  - Author  
  - ISBN  
  - Publication date  
  - Availability status  
- Books are displayed dynamically on both admin and user dashboards.

---

### **Borrowing and Returning System**
- Users can borrow available books and return borrowed books through a dedicated return form.
- Borrowed books are linked to both the **user** and a **transaction record**.
- Each transaction includes:
  - Borrow date  
  - Return due date  
  - Returned status  
- When a book is returned, the system automatically updates its availability in the database.
- Proper validation ensures unavailable books cannot be borrowed again until returned.

---

### **Transaction Management**
- Each borrowing and return action is tracked in the `Transaction` model.
- Admins can view and update transaction details.
- The system ensures only valid user-book pairs are processed during borrowing or returning.
- The update functionality is implemented using **API views** that handle `PUT` or `PATCH` requests for modifying transaction details.

---

### **API Endpoints**
- RESTful API endpoints are available for key functionalities such as:
  - Listing all books (`GET`)
  - Creating new book records (`POST`)
  - Updating or deleting specific books (`PUT`, `DELETE`)
  - Managing transactions and book returns through the API
- Authentication and permission handling ensure secure access to API resources.

---

### **Admin Dashboard**
- Displays system statistics such as:
  - Total number of books  
  - Books currently borrowed  
  - Returned books  
  - Active users  
  - Recently added books
- Provides quick access to manage library items and monitor borrowing activity.

---

### **User Dashboard**
- Displays:
  - List of books available for borrowing  
  - User’s borrowing and return history  
  - Notifications about borrowed or overdue books
- Clean and responsive design for better user experience.

---

### **Frontend Integration**
- Uses Django templates and static files for UI rendering.
- Includes a consistent base layout with navigation and message display.
- CSS designed for clear visual separation between admin and user interfaces.

---

### **Logout Functionality**
- Implemented using Django’s built-in `LogoutView`.
- Clears user sessions and redirects to the login page with a logout success message.
