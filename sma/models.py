from django.db import models

# Create your models here.
class School(models.Model):

    name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30,null=True,blank=True)
    state = models.CharField(max_length = 30,null=True,blank=True)
    phone = models.CharField(max_length = 30,null=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self) -> str:
        return f"{self.name}"


class Student(models.Model):

    GENDER_CHOICES = (
        ("Male","Male"),
        ("Female","Female")
    )

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30,null=True,blank=True)
    email = models.EmailField(max_length = 30,unique=True)
    gender = models.CharField(max_length=7,choices=GENDER_CHOICES,null=True,blank=True)
    school = models.ForeignKey(School,on_delete =models.SET_NULL,null=True,blank = True,related_name="student")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=30,unique = True)
    total_pages = models.IntegerField(null = True, blank= True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return f"{self.name}"



class ViewedBooks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="viewed_books")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="viewed_books")
    pages_read_count = models.IntegerField(null = True,blank = True,default=0)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Viewed Books Data"
        verbose_name_plural = "Viewed Books Data"

    def __str__(self) -> str:
        return f"{self.book} ::: {self.student}"