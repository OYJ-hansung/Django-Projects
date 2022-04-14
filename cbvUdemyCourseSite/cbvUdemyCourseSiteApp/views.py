from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from cbvUdemyCourseSiteApp.models import Course
from django.urls import reverse_lazy


class CourseListView(ListView):
    model = Course
    #default template_name is course_list.html
    #default context_object_name is course_list

class CourseDetailView(DetailView):
    model = Course
    #default template_name is course_detail.html
    #default context_object_name is student

class CourseCreateView(CreateView):
    model = Course
    fields = {'name', 'description', 'instructor', 'rating'}
    #default template_name is course_form

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses')

class CourseUpdateView(UpdateView):
    model = Course
    fields = {'name', 'description', 'instructor', 'rating'}
