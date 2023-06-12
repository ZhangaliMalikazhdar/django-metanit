from .models import *


print(Product.objects.get(id=3).company.id)

print(Product.objects.get(id=2).company.name)

apple = Product.objects.filter(company__name='apple')

print(apple.values_list)

apple = Company.objects.get(name='apple')
print(apple.product_set.all())
print(apple.product_set.count())
print(apple.product_set.filter(name__startswith='mac'))


oppo = Company.objects.create(name='Oppo')
oppo.product_set.create(name='Oppo 2020', price=1000)
oppoX = Product(name='OppoX', price=2300)
oppo.product_set.add(oppoX, bulk=False)

o = Company.objects.get(name='Oppo')
print(o.product_set.filter(name__endswith='X'))
