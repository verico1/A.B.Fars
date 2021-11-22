from django.core.checks import messages
from django.shortcuts import render
from products.models import Category, Product
from main.models import Message, IPAddress
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def staff_index(request):
    this_year = time.strftime("%Y", time.localtime(time.time()))
    this_month = time.strftime("%m", time.localtime(time.time()))
    this_day = time.strftime("%d", time.localtime(time.time()))

    products_count = Product.objects.all().count()
    messages_count = Message.objects.all().count()

    views_of_month_count = IPAddress.objects.filter(created_on__year=this_year ,created_on__month=this_month).count()
    messages_of_month_count = Message.objects.filter(created_on__year=this_year ,created_on__month=this_month).count()

    views_of_day_count = IPAddress.objects.filter(created_on__year=this_year ,created_on__month=this_month, created_on__day=this_day).count()
    ctx = {
        'products_count':products_count,
        'messages_count':messages_count,
        'messages_of_month_count':messages_of_month_count,
        'views_of_month_count':views_of_month_count,
        'views_of_day_count':views_of_day_count
    }
    return render(request, "staff/home.html", ctx)

def staff_messages(request):
    messages = Message.objects.order_by('-created_on', '-created_on_time')
    count = Message.objects.all().count()
    page = request.GET.get('page', 1)
    paginator = Paginator(messages, 12)
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)
    ctx = {'messages':messages, 'count':count}
    return render(request, 'staff/messages.html',ctx)   

def staff_categories(request):
    if request.method == "POST":
        category_name_fa = request.POST['category_name_fa']
        category_name_en = request.POST['category_name_en']
        category_name_ku = request.POST['category_name_ku']
        category_name_ar = request.POST['category_name_ar']
        try:
            category_name = Category.objects.get(category_fa=category_name_fa,
                category_en=category_name_en,
                category_ku=category_name_ku,
                category_ar=category_name_ar)
        except Category.DoesNotExist:
            category_name = Category(category_fa=category_name_fa,
                category_en=category_name_en,
                category_ku=category_name_ku,
                category_ar=category_name_ar)  
            category_name.save()
    categories = Category.objects.all()
    count = Category.objects.all().count()
    page = request.GET.get('page', 1)
    paginator = Paginator(categories, 12)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    ctx = {'categories':categories, 'count':count}
    return render(request, "staff/categories.html", ctx)        

def staff_products(request):
    products = Product.objects.all()
    count = Message.objects.all().count()
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    ctx = {'products':products, 'count':count}
    return render(request, "staff/products.html", ctx)  

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = "staff/create_product.html"

def staff_create_products(request):
    return render(request, "staff/create_product.html")     

def staff_settings(request):
    return render(request, "staff/settings/settings.html")