from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),  
    path('getTypes/', views.getTypes, name='types'),
    path('getProducts/', views.getProducts, name='products'),
    path('productDetails/<int:id>', views.productDetails, name='productdetails'),
    path('newProduct', views.newProduct, name='newproduct'),
    path('newReview', views.newReview, name='newreview'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]