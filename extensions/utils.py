from . import jalali


def jalali_converter(time):
	time_to_str = "{},{},{}".format(time.year, time.month, time.day)
	time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
	j_months = ["فروردین",
		"اردیبهشت",
		"خرداد",
		"تیر",
		"مرداد",
		"شهریور",
		"مهر",
		"آبان",
		"آذر",
		"دی",
		"بهمن",
		"اسفند",]
	return "{} {} {}".format(time_to_tuple[0], j_months[time_to_tuple[1]-1], time_to_tuple[2]), time_to_tuple, f"{time_to_tuple[2]}/{time_to_tuple[1]}"