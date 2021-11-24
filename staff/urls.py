from django.urls import path
from . import views

app_name="staff"
urlpatterns = [
    path('', views.staff_index, name="staff_index"),
    path('messages/', views.staff_messages, name="staff_messages"),
    path('message/<id>/', views.staff_message, name="staff_message"),
    path('categories/', views.staff_categories, name="staff_categories"),
    path('products/', views.staff_products, name="staff_products"),
    path('create-product/', views.CreateProduct.as_view(), name="staff_create_products"),
    path('update-product/<pk>/', views.UpdateProduct.as_view(), name="staff_update_products"),
    path('delete-product/<id>/', views.delete_product, name="staff_delete_product"),
    path('settings/', views.staff_settings, name="staff_settings"),
]
