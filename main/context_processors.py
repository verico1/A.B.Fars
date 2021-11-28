from settings.models import Setting
from products.models import Product
import random

def setting(requet, **kwargs):
    setting = Setting.objects.first()
    random_products = Product.objects.all()
    ctx = {'setting':setting,
        'random_products':random_products,
        }
    return ctx