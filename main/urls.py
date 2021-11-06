from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('', views.index, name="index"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('about-us/', views.about_us, name="about_us"),
]
