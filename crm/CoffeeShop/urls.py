from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customers/<str:pk>/',views.customers, name="customer"),
    path('products/',views.products, name="products"),
]
