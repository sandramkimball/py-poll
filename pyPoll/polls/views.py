from django.shortcuts import render

from .models import Choice, Question

# Get questions and display them
def index(request):
    # this loads the template
    return render(request, 'polls/index.html')