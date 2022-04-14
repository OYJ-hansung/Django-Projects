from django.contrib import admin
from django.urls import path
from cbvUdemyCourseSiteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('create/', views.CourseCreateView.as_view()),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view()),
    path('update/<int:pk>/', views.CourseUpdateView.as_view())
]
