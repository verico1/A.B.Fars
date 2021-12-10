from django.shortcuts import get_object_or_404, render
from django.contrib import messages

# models imported here
from .models import IPAddress, Message
from settings.models import Setting
from products.models import Category, Product

# Translation Imports
from django.utils.translation import gettext as _

def index(request):
	"""
		products are here
	"""
	products = Product.objects.all()
	categories = Category.objects.all()
	"""
		settings are here
	"""
	setting = Setting.objects.first()
	"""
		Contact us section exsists here
		request form is POST, and also validators placed for each input
	"""
	if request.method == "POST":
		name = request.POST['name']
		phone_number = request.POST['phone_number']
		text = request.POST['text']
		email = request.POST['email']
		if len(name) > 60:
			messages.error(request, _('خطا در ثبت پیام. لطفا نام و نام خانوادگی را صحیح وارد کنید'))
		elif not len(phone_number) == 11 or not phone_number.isdigit():
			messages.error(request, _('خطا در ثبت پیام. لطفا شماره تماس را صحیح وارد کنید'))
		elif len(text) > 1000:
			messages.error(request, _('خطا در ثبت پیام. لطفا متن پیام را کوتاه تر کنید'))
		else:
			message = Message(name=name, email=email, phone_number=phone_number, text=text)
			message.save()
			messages.success(request, 'پیام با موفقیت ارسال شد')
	ctx = {'setting':setting, 'products':products, 'categories':categories}
	return render(request, 'main/index.html', ctx)

def product(request, id):
	product = get_object_or_404(Product, id=id)
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	ip_address = IPAddress.objects.get(ip_address=ip)			
	if ip_address not in product.hits.all():
		product.hits.add(ip_address)
	ctx = {'product':product}
	return render(request, "main/product.html", ctx)

