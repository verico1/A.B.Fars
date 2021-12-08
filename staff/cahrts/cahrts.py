from main.models import IPAddress
import time
from extensions.utils import jalali_converter
from extensions import jalali

def site_views_month():
    this_year = time.strftime("%Y", time.localtime(time.time()))
    this_day = time.strftime("%d", time.localtime(time.time()))
    i = 0
    counts = []
    while i < 12:
        i += 1
        time_to_str = "{},{},{}".format(this_year, i, this_day)
        date = jalali.Gregorian(time_to_str).persian_tuple()
        view_count = IPAddress.objects.filter(created_on__year=this_year ,created_on__month=i).count()
        counts.insert(date[1]-1, view_count)
    return counts