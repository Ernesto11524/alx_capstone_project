from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

# This is a custom user model that add additional fields to the built-in User Model.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher')
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    other_names = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.other_names}"
    

# This model handle the major programs done in the school
class Programs(models.Model):
    PROGRAMS = (
        ('General Science', 'General Science'),
        ('General Arts', 'General Arts'),
        ('Visual Arts', 'Visual Arts'),
        ('Business', 'Business')
    )
    program_name = models.CharField(max_length=30, choices=PROGRAMS)

    def __str__(self):
        return self.program_name
    

# This is a model about the various classes in the school.
class Classroom(models.Model):
    CLASSES = (
        ('SHS 1', 'SHS 1'),
        ('SHS 2', 'SHS 2'),
        ('SHS 3', 'SHS 3')
    )
    class_name = models.CharField(max_length=10, choices=CLASSES)

    def __str__(self):
        return self.class_name


# This is a model for students in the school.
class Student(models.Model):
    count = 2
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Student'})
    studentID = models.CharField(max_length=10, unique=True, blank=True)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=10)
    program = models.ForeignKey(Programs, on_delete=models.SET_NULL, related_name='p_students', null=True)
    year = models.ForeignKey(Classroom, on_delete=models.SET_NULL, related_name='y_students', null=True)

    def __str__(self):
        return f"{self.studentID}, {self.student}"
    
    
    # This method handles the student's ID. It automatically creates and ID for a student when it is created
    # and also saves the student in the database.
    def save(self, *args, **kwargs):
        if not self.studentID:
            current_year = datetime.now().year

            last_student = Student.objects.filter(
                studentID__startswith=f"STU-{current_year}"
            ).order_by('studentID').last()

            if last_student:
                last_number = int(last_student.studentID.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1

            number_str = str(new_number).zfill(4)

            self.studentID = f"STU-{current_year}-{number_str}"

        return super().save(*args, **kwargs)


# This model talks about some of the subjects taught by a teacher in the school.
class Subject(models.Model):
    SUBJECT = (
        ('English Language', 'English Language'),
        ('Core Mathematics', 'Core Mathematics'), 
        ('Integrated Science', 'Integrated Science'),
        ('Social Studies', 'Social Studies'),
        ('Biology', 'Biology'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Elective Mathematics', 'Elective Mathematics')
    )
    subject_name = models.CharField(max_length=50, choices=SUBJECT)

    def __str__(self):
        return self.subject_name



# This model handle the creation of teachers in the school.
class Teacher(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Teacher'})
    teacherID = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.teacher}, {self.teacherID}"
    

    # This method also generate teacher's ID automaticatlly.
    def save(self, *args, **kwargs):
        current_year = datetime.now().year

        last_teacher = Teacher.objects.filter(
            teacherID__startswith=f"TCH-{current_year}"
        ).order_by('teacherID').last()

        if last_teacher:
            last_number = int(last_teacher.teacherID.split('-')[-1])
            new_number = last_number + 1

        else:
            new_number = 1

        number_str = str(new_number).zfill(3)
        self.teacherID = f"TCH-{current_year}-{number_str}"

        return super().save(*args, **kwargs)