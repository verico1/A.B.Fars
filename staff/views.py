from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView
from translated_fields import fields
from products.models import Category, Product
from main.models import Message, IPAddress
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from settings.models import Setting
from staff.cahrts.cahrts import site_views_month

from extensions.im_not_robot import grecaptcha_verify

# Create your views here.
def staff_index(request):
    if request.user.is_staff:
        this_year = time.strftime("%Y", time.localtime(time.time()))
        this_month = time.strftime("%m", time.localtime(time.time()))
        this_day = time.strftime("%d", time.localtime(time.time()))

        products_count = Product.objects.all().count()
        messages_count = Message.objects.all().count()
        readed_messages_count = Message.objects.filter(is_read=False).count()

        views_of_month_count = IPAddress.objects.filter(created_on__year=this_year ,created_on__month=this_month).count()
        messages_of_month_count = Message.objects.filter(created_on__year=this_year ,created_on__month=this_month).count()

        views_of_day_count = IPAddress.objects.filter(created_on__year=this_year ,created_on__month=this_month, created_on__day=this_day).count()
        
        products = Product.objects.all()
        ctx = {
            'products_count':products_count,
            'messages_count':messages_count,
            'messages_of_month_count':messages_of_month_count,
            'views_of_month_count':views_of_month_count,
            'views_of_day_count':views_of_day_count,
            'readed_messages_count':readed_messages_count,
            'cahrt_counts':site_views_month(),
            'products':products,
        }
        return render(request, "staff/home.html", ctx)
    else:
        return redirect("/staff/login/")    

def staff_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not grecaptcha_verify(request):
            ctx = {'msg_bad':'لطفا تست ربات را کامل کنید'}
        elif user is not None:
            login(request, user)
            return redirect('/staff/')
        else:
            ctx = {'msg_bad':'نام کاربری یا کلمه عبور اشتباه است'}
        return render(request, 'staff/login.html/', ctx)
    return render(request, 'staff/login.html/')

def staff_logout(request):
    if request.user.is_staff:
        logout(request)
        return redirect("/staff/")
    else:
        return redirect("/staff/login/")    

def staff_messages(request):
    if request.user.is_staff:
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
    else:
        return redirect("/staff/login/")        

def staff_message(request, id):
    if request.user.is_staff:
        message = get_object_or_404(Message, id=id)
        message.is_read = True
        message.save()
        ctx = {'message':message}
        return render(request, 'staff/message.html', ctx)
    else:
        return redirect("/staff/login/")  

def staff_categories(request):
    if request.user.is_staff:
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
    else:
        return redirect("/staff/login/")  

def staff_products(request):
    if request.user.is_staff:
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
    else:
        return redirect("/staff/login/")  

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = "staff/create_product.html"

def delete_product(request, id):
    if request.user.is_staff:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("/staff/products/")
    else:
        return redirect("/staff/login/")      

class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = "staff/create_product.html"

def staff_settings(request):
    if request.user.is_staff:
        if request.method == "POST":
            setting = Setting.objects.first()
            setting.title_fa = request.POST['title_fa']
            setting.title_ku = request.POST['title_ku']
            setting.title_en = request.POST['title_en']
            setting.meta_title_fa = request.POST['meta_title_fa']
            setting.title_ar = request.POST['title_ar']
            setting.meta_title_ar = request.POST['meta_title_ar']
            setting.meta_title_ku = request.POST['meta_title_ku']
            setting.meta_title_en = request.POST['meta_title_en']
            setting.about_us_fa = request.POST['about_us_fa']
            setting.about_us_ar = request.POST['about_us_ar']
            setting.about_us_ku = request.POST['about_us_ku']
            setting.about_us_en = request.POST['about_us_en']
            setting.about_us_small_fa = request.POST['about_us_small_fa']
            setting.about_us_small_ar = request.POST['about_us_small_ar']
            setting.about_us_small_ku = request.POST['about_us_small_ku']
            setting.about_us_small_en = request.POST['about_us_small_en']
            setting.address_fa = request.POST['address_fa']
            setting.address_ar = request.POST['address_ar']
            setting.address_ku = request.POST['address_ku']
            setting.address_en = request.POST['address_en']
            setting.email = request.POST['email']
            setting.instagram = request.POST['instagram']
            setting.telegram = request.POST['telegram']
            setting.whatsapp = request.POST['whatsapp']
            setting.save()

            """
                numeric data
            """
            setting.products_count = request.POST['products_count']
            setting.international_customers = request.POST['international_customers']
            setting.years_of_activity = request.POST['years_of_activity']
            setting.domestic_customers = request.POST['domestic_customers']
            setting.save()
        settings = Setting.objects.first()
        ctx = {'settings':settings}
        return render(request, "staff/settings/settings.html", ctx)
    else:
        return redirect("/staff/login/")  

def delete_category(request, id):
    if request.user.is_staff:
        category = Category.objects.get(id=id)
        category.delete()
        return redirect("/staff/categories")    
    else:
        return redirect("/staff/login/")          
