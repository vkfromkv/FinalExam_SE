from django.shortcuts import render
from .models import Course  # Import the correct model from your app

def course_list(request):
    """
    View function to render a list of courses.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying a list of courses.
    """
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
