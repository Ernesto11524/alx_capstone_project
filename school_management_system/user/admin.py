from django.contrib import admin
from .models import CustomUser, Student, Teacher, Programs, Classroom, Subject
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Since a custom user model was created, a custom user admin also had to be created to include the additional fields
# added to the custom user model.
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'other_names', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'other_names')
    ordering = ('last_name', 'other_names', 'first_name')

    fieldsets = (
        ('Names', {'fields': ('first_name', 'last_name', 'other_names',)}),
        ('Other Info', {'fields': ('username','email', 'gender', 'date_of_birth', 'role',)}),
    )

    add_fieldsets = (
        ('Names', {'fields': ('first_name', 'last_name', 'other_names',)}),
        ('Other Info', {'fields': ('username','email', 'gender', 'date_of_birth', 'role', 'password1', 'password2')}),
    )


# A student admin had to be created to exclude the student ID field since the program will automatically generate it.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'student', 'program', 'year')
    ordering = ('studentID',)
    search_fields = ('studentID', 'student', 'program', 'year')
    list_filter = ('program', 'year')

    fields = ('student', 'program', 'year', 'guardian_name', 'guardian_contact')


# A teacher admin had to be created to exclude the teacher ID field since the program will automatically generate it.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacherID', 'teacher', 'subject', 'phone_number')
    ordering = ('teacherID',)
    search_fields = ('teacherID', 'teacher', 'subject', 'phone_number')
    list_filter = ('subject',)

    fields = ('teacher', 'subject', 'phone_number')


# This registers the models in the admin panel.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Programs)
admin.site.register(Classroom)
admin.site.register(Subject)