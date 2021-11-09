from django.shortcuts import render
from django.contrib import messages

# models imported here
from .models import Message

# Translation Imports
from django.utils.translation import gettext as _

def index(request):
	"""
		Contact us section exsists here
		request form is POST, and also validators placed for each input
	"""
	if request.method == "POST":
		name = request.POST['name']
		phone_number = request.POST['phone_number']
		text = request.POST['text']
		if len(name) > 60:
			messages.error(request, 'خطا در ثبت پیام. لطفا نام و نام خانوادگی را صحیح وارد کنید')
		elif not len(phone_number) == 11 or not phone_number.isdigit():
			messages.error(request, 'خطا در ثبت پیام. لطفا شماره تماس را صحیح وارد کنید')
		elif len(text) > 1000:
			messages.error(request, 'خطا در ثبت پیام. لطفا متن پیام را کوتاه تر کنید')
		else:
			message = Message(name=name, phone_number=phone_number, text=text)
			message.save()
			messages.success(request, 'پیام با موفقیت ارسال شد')
	return render(request, 'main/index.html')

def about_us(request):
	return render(request, 'main/about-us.html')
