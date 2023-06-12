from .models import Order, Person
from datetime import datetime, date, time


if Order.objects.count() == 0:
    Order.objects.create(datetime=datetime(2021, 12, 26, 11, 25, 34))
    Order.objects.create(datetime=datetime(2022, 5, 12, 12, 25, 34))
    Order.objects.create(datetime=datetime(2022, 5, 22, 13, 25, 34))
    Order.objects.create(datetime=datetime(2022, 8, 19, 14, 25, 34))

orders = Order.objects.filter(datetime__month=5)
for order in orders:
    print(order)
print()
orders = Order.objects.filter(datetime__month__gt=5)
for order in orders:
    print(order)
print()
orders = Order.objects.filter(datetime__date=date(2022, 5, 22))
for order in orders:
    print(order)
print()
orders = Order.objects.filter(datetime__time__gt=time(12, 20, 0))
for order in orders:
    print(order)

print(Person.objects.filter(name="Bob") & Person.objects.filter(age__range=(1, 50)))
print(Person.objects.filter(name="Tom") | Person.objects.filter(age=10))
print(Person.objects.filter(name="Tom") ^ Person.objects.filter(age=22))
