
from django.shortcuts import render
from .models import Textbook

def textbook_list(request, course_code):
    # Retrieve textbooks based on course code and availability
    textbooks = Textbook.objects.filter(course_code=course_code, available=True)
    
    # Check for search query
    search_query = request.GET.get('search', '')
    if search_query:
        textbooks = textbooks.filter(
            title__icontains=search_query) | textbooks.filter(
            author__icontains=search_query) | textbooks.filter(
            edition__icontains=search_query)
    
    return render(request, "textbooks/list.html", {
        "textbooks": textbooks,
        "course_code": course_code,
        "search_query": search_query,
    })