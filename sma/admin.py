from django.contrib import admin
from sma.models import School, Student, Book, ViewedBooks
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'phone')
    list_filter = ('name','city', 'state')
    search_fields = ('name', 'city', 'state', 'phone')
    ordering = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','gender','school')
    list_filter = ('school','gender')
    search_fields = ('first_name', 'last_name', 'email', 'school')
    ordering = ['first_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','total_pages')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['name']

@admin.register(ViewedBooks)
class ViewedBooksAdmin(admin.ModelAdmin):
    list_display = ('student','book','pages_read_count')
    list_filter = ('student','book')
    search_fields = ('student','book')
    ordering = ['student']