from django.urls import path
from . import views

app_name="staff"
urlpatterns = [
    path('', views.staff_index, name="staff_index"),
    path('messages/', views.staff_messages, name="staff_messages"),
    path('categories/', views.staff_categories, name="staff_categories"),
    path('products/', views.staff_products, name="staff_products"),
    path('create-product/', views.CreateProduct.as_view(), name="staff_create_products"),
    path('settings/', views.staff_settings, name="staff_settings"),
]
