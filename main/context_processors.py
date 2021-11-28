from settings.models import Setting
from products.models import Product
import random

def setting(requet, **kwargs):
    setting = Setting.objects.first()
    products = Product.objects.all()
    random_products = random.sample(list(products), 3)
    ctx = {'setting':setting,
        'random_products':random_products,
        }
    return ctx