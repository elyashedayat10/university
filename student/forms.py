from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = (
            'full_name',
            'created',
            'updated',
            'creator'
        )
        labels = {
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "national_code": "کد ملی",
            "father_name": "نام پدر",
            "phone_number": "شماره تماس",
            "father_phone_number": "شماذه تماس پدر",
            "mother_phone_number": "شماره تماس مادر",
            'second_number': "شماره نماس",
        }
