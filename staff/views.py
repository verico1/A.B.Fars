from django.shortcuts import render

# Create your views here.
def staff_index(request):
    return render(request, "staff/home.html")