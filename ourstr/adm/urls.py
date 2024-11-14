
from django.urls import path,include
from .import views
from .views import product_list

urlpatterns = [
   
      path('',views.home,name='home'),
      path('register/',views.register,name='register'),
      path('login/',views.login_view,name='login'),
      path('home2/',views.home2,name='home2'),
      path('logout/',views.logout_view,name='logout'),
      path('insight/home', views.home2,name='home2'),
      path('insight/product', views.product_list,name='product_list'), 
      

      # path('home2/products/', views.product_list, name='product_list'),
      path('home2/products/', views.product_list, name='product_list'),
]

