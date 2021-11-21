from django.shortcuts import render
from django.contrib import messages

# models imported here
from .models import Message
from settings.models import Setting

# Translation Imports
from django.utils.translation import gettext as _

def index(request):
	"""
		settings are here
	"""
	setting = Setting.objects.first()
	ctx = {'setting':setting}
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
	return render(request, 'main/index.html', ctx)

