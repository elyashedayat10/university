from django.urls import path
from .views import MasterListView

app_name = "master"
urlpatterns = [
    path("list/", MasterListView.as_view(), name="master_list")
]
