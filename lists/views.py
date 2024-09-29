from django.shortcuts import render
from django.urls import reverse
from .models import TaskView
from .forms import TaskForm
from django.views.generic import ListView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from jalali_date import date2jalali,datetime2jalali
# Create your views here.

class TaskListView(ListView):
    model = TaskView
    template_name = "lists/task-lists.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = TaskView
    form_class = TaskForm
    template_name = "lists/form-list.html"
    success_url = "/thank-you"


    


class ThankyouView(TemplateView):
    template_name = "lists/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["massage"] = "This works!"
        return context

    



class TaskUpdateView(UpdateView):
    model = TaskView
    form_class = TaskForm
    template_name = "lists/form-list.html"
    success_url = "/thank-you"
    

class TaskDeleteView(DeleteView):
    model = TaskView
    template_name = "lists/form-delete.html"
    success_url = "/thank-you"
