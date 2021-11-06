from django.shortcuts import render

# Translation Imports
from django.utils.translation import gettext as _

def index(request):
	return render(request, 'main/index.html')

def contact_us(request):
	return render(request, 'main/contact-us.html')

def about_us(request):
	return render(request, 'main/about-us.html')
