from django.urls import path
from . import views

app_name="staff"
urlpatterns = [
    path('', views.staff_index, name="staff_index"),
]
