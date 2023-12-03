from django.shortcuts import render
from .models import Course  # Import the correct model from your app

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
