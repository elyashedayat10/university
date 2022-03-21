from django.urls import path
from .views import StudentListView,StudentCreateView

app_name = "student"
urlpatterns = [
    path('list/', StudentListView.as_view(), name="student_list"),
    path('create/', StudentCreateView.as_view(), name="student_create"),
]
