from django.db.models import F
from sma.models import Student, Book, ViewedBooks

class StudentHandler:

    @classmethod
    def get_details_of_student(cls,student_id = None, student_name = None):

        filter_kwargs_student = {}
        filter_kwargs_viewed_books = {}

        if student_id:
            filter_kwargs_student['id'] = student_id
            filter_kwargs_viewed_books['student__id'] = student_id
            filter_kwargs_viewed_books["pages_read_count__gt"] = 0

        if student_name:
            filter_kwargs_student['first_name__icontains'] = student_name
            filter_kwargs_viewed_books['student__first_name__icontains'] = student_name
            filter_kwargs_viewed_books["pages_read_count__gt"] = 0


        student = list(Student.objects.filter(**filter_kwargs_student).values("first_name",
                                                        "last_name","email",
                                                        "school__name","gender"))

        viewed_book_details = list(ViewedBooks.objects.filter(**filter_kwargs_viewed_books) \
                            .annotate(read_book_name = F("book__name"),pages_read = F("pages_read_count"))
                            .values("read_book_name","pages_read"))
    
        student_details = {}
        if len(student) != 0:

            student_details["first_name"] = student[0]["first_name"]
            student_details["last_name"] = student[0]["last_name"]
            student_details["email"] = student[0]["email"]
            student_details["school"] = student[0]["school__name"]
            student_details["gender"] = student[0]["gender"]
            student_details["read_books"] = viewed_book_details

        return student_details

