from django.urls import path
from .views import insight_view

urlpatterns = [
    path('', insight_view, name='insight'),  # Match to /insight/
]
