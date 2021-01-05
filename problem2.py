from datetime import date
f_date = date(2020, 7, 2)
l_date = date(2020, 7, 11)
delta = l_date - f_date
print(delta.days)

# (20200702), (20200711)