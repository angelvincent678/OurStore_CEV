


from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.http import HttpResponse

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the feedback directly
            return HttpResponse("<h1>Feedback has been submitted</h1>")
    else:
        form = FeedbackForm()  # Create a new empty form instance
    return render(request, 'home2.html', {'form': form})
