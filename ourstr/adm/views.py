from django.shortcuts import render,redirect,get_object_or_404
from feedback.models import Feedback
# from django.http import Http
# from django.http import JsonResponsepResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import RegistrationForm,LoginForm
from .models import Customer
from .models import Product
from django.db.models import Q  # To allow complex queries
from django.contrib import messages
# from .forms import SaleForm


# Create your views here.
def home(request):
      return render(request,'home.html')



def home2(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:

      products = Product.objects.filter(
      Q(name__icontains=query) | Q(description__icontains=query)  # Search in name and description
      )
    else:
        products = Product.objects.all()  # Show all products if no search term

    return render(request,'home2.html',{'products':products, 'query': query})


    




def register(request):
      if request.method == 'POST':
            form =RegistrationForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  #create a profile
                  Customer.objects.create(
                        user=user,
                        phone_number=form.cleaned_data.get('phone_number'),
                        register_no=form.cleaned_data.get('register_no')
                  )
                  return redirect('login')
      else:
            form = RegistrationForm()
      return render(request,'register.html',{'form':form})

def login_view(request):
      if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(request,username=username,password=password)
                  if user is not None:
                        login(request,user)
                        return redirect('home2')
                  else:
                        #invalid credentials
                        pass
      else:
            form = LoginForm()
      return render(request,'login.html',{'form':form})



def product_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)  # Search in name and description
        )
    else:
        products = Product.objects.all()  # Show all products if no search term
   
    return render(request, 'products/product_list.html', {'products': products, 'query': query})





def logout_view(request):
      logout(request)
      return redirect('home')






