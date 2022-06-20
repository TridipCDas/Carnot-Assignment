from django import forms
from sma.models import Student, School, Book

class StudentSearchForm(forms.Form):
    student_id = forms.IntegerField(required=False,label="Student ID")
    student_name = forms.CharField(required=False,label="Student Name")

    def clean(self):

        cleaned_data = super(StudentSearchForm, self).clean()
        student_id = cleaned_data.get("student_id")
        student_name = cleaned_data.get("student_name")

        if not student_id and not student_name:
            raise forms.ValidationError("Please enter either Student ID or Student Name")

        return cleaned_data


class StudentCreateForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.all(),required=False)

    class Meta:
        model = Student
        fields = "__all__"

    def clean(self):
        cleaned_data = super(StudentCreateForm, self).clean()
        email = cleaned_data.get("email")
        email_qry = Student.objects.filter(email__iexact = email)
        if email_qry.exists():
            raise forms.ValidationError("This email is already registered. Please select a different email.")
        return cleaned_data