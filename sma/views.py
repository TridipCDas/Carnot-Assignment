from django.shortcuts import render
from django.views.generic import TemplateView

from sma.utility.student_handler import StudentHandler
from sma.models import Student, Book
from sma.forms import StudentSearchForm, StudentCreateForm

class StudentDetailView(TemplateView):
    template_name = "sma/student_detail.html"

    def __init__(self):
        super(StudentDetailView, self).__init__()
        self.student = None

    def get(self,request,*args,**kwargs):
        student_qry = Student.objects.filter(id=kwargs['id'])
        if student_qry.exists():
            self.student = kwargs['id']

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self,*args,**kwargs):
        context = super(StudentDetailView, self).get_context_data(*args,**kwargs)
        context["error"] = False
        if self.student:
            context['student_exists'] = True
            context['student_details'] = StudentHandler.get_details_of_student(self.student)
        else:
            context['student_exists'] = False
            context['student_details'] = []
        return context


def student_search_view(request):

    if request.method == "POST":
        form = StudentSearchForm(request.POST)

        if form.is_valid():
            student_id = form.cleaned_data.get("student_id")
            student_name = form.cleaned_data.get("student_name")

            if student_id:
                student_details = StudentHandler.get_details_of_student(student_id=student_id)
            else:
                student_details = StudentHandler.get_details_of_student(student_name=student_name)

            students_data = {"student_exists":False, "student_details":student_details}
            if student_details:
                students_data["student_exists"] = True

            return render(request,"sma/student_detail.html",students_data)
        else:
            return render(request,"sma/student_search.html",{"form":form})



    elif request.method == "GET":
        form = StudentSearchForm()

        return render(request, 'sma/student_search.html', {'form': form})


def create_student_view(request):
    
    if request.method == "POST":
        form = StudentCreateForm(request.POST)

        if form.is_valid():
            student = form.save()
            book_values = [key for key in request.POST if key.startswith("book")]

            for book in book_values:
                _,_ = Book.objects.get_or_create(name__iexact=request.POST[book])

            return render(request,"sma/student_detail.html",{"student_exists":True, "student_details":StudentHandler.get_details_of_student(student.id)})

    elif request.method == "GET":
        form = StudentCreateForm()
        books = list(Book.objects.all().values_list("name", flat=True))
        return render(request, 'sma/student_create.html', {'form': form, 'books': books})