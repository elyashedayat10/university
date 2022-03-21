from django.shortcuts import render
from django.views.generic import ListView,View,UpdateView,CreateView
from .models import Master
# Create your views here.
class MasterListView(ListView):
    model = Master
    template_name = "list.html"