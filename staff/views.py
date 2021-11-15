from django.shortcuts import render

# Create your views here.
def staff_index(request):
    return render(request, "staff/home.html")

def staff_messages(request):
    return render(request, "staff/messages.html")    

def staff_categories(request):
    return render(request, "staff/categories.html")        

def staff_products(request):
    return render(request, "staff/products.html")  

def staff_create_products(request):
    return render(request, "staff/create_product.html")     

def staff_settings(request):
    return render(request, "staff/settings/settings.html")