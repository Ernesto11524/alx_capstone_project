# alx_capstone_project

# Student Management System (Django)

This project is a **Student Management System** built with Django and Django Rest Framework. The goal is to manage students, staff and academic details in a structured way while learning Django concepts step by step.

- - -

## Features Implemented So Far

- **Custom User Model**
    Extended the default Django `AbstractUser` to add fields like `other_names`, `date_of_birth`, `gender` and `role` for different types of users (Admin, Student, Teacher).

- **Student Model**
    - Linked to the custom user with a `OneToOneField`.
    - Include details like:
        - Guardian information
        - Program of study
        - Year/classroom assignment
    - Auto-generates a unique **Student ID** in the format:
    ```
    STU-<current_year>-<number>
    ```

- **Programs & Classroom Models**
    - `Programs` model to store courses of study.
    - `Classroom` model to represent year levels or classes.
    - Both linked to students with `ForeignKey` relationships.

- **Teacher Model**
    - Linked to custom user with a `OneToOneField`.
    - Includes details like:
        - Teacher's personal information like phone_number.
        - The subject the teacher teaches.
    - Auto-generated a unique **Teacher ID** in the format:
    ```
    TCH-<current_year>-<number>
    ```

- **Subject Model**
    - The subject model contains the subjects taught in the school and each teacher is assigned one.
    - Linked to the teacher's model.

- **Admin Panel Customization**
    - Registered models in the admin panel.
    - Customized the displayed fields for better readability.