from django.shortcuts import render, redirect
from courseApp import views
from courseApp.models import Course
from courseApp.forms import CourseForm

# Create your views here.
def getCourses(request):
    courses = Course.objects.all()
    return render(request, 'courseApp/index.html', {'courses': courses})

def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'courseApp/create.html', {'form':form})

def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def updateCourse(request , id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance = course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance = course)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'courseApp/update.html', {'form':form})


