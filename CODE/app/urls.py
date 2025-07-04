from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('uploadproduct', views.uploadproduct, name='uploadproduct'),
    path('products', views.products, name='products'),
    path('viewproduct/<int:id>', views.viewproduct, name='viewproduct'),
    path('furniture', views.furniture, name='furniture'),
    path('clothing', views.clothing, name='clothing'),
    path('electronics', views.electronics, name='electronics'),
    path('books', views.books, name='books'),
    path('shoes', views.shoes, name='shoes'),
    path('viewprofile/<str:mail>', views.viewprofile, name='viewprofile'),
    path('chat/<int:id>/<str:mail>', views.chat, name='chat'),
    path('viewchats', views.viewchats, name='viewchats'),
    path('getproduct/<int:id>', views.getproduct, name='getproduct'),
    path('collectedproducts', views.collectedproducts, name='collectedproducts'),
    path('viewusers', views.viewusers, name='viewusers'),
    path('acceptusers/<int:id>', views.acceptusers, name='acceptusers'),
    path('producttransactions', views.producttransactions, name='producttransactions'),

    
]
