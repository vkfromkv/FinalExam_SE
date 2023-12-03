from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mscs_courses.models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})