from django.urls import path
from . import views

urlpatterns = [
    path('home2/feedback/', views.feedback, name="feedback"),  
]
