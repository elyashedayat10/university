from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, View
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = "student/list.html"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("config:panel")
    template_name = "student/forms_wizard.html"
