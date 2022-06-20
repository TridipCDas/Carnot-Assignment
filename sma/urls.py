from django.urls import path
from . import views

urlpatterns = [
    path("<str:id>",views.StudentDetailView.as_view(),name="student_detail"),
    path("search/",views.student_search_view,name="student_search"),
    path("create/",views.create_student_view,name="student_create")
]