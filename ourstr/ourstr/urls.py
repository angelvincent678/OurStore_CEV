"""
URL configuration for ourstr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from adm.views import home2
# from reports.admin import admin_site  # Import custom admin site



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('adm.urls')),
    path('',include('adm.urls')),
    path('feedback/',include('feedback.urls')),
    
    
    # path('booking/', include('booking.urls')),  # Include booking app URLs
    path('insight/', include('insights.urls')),
    
]
