from .models import Person
from django.db.models import F


# number = Person.objects.filter(id=1).update(name='Mike')
# Person.objects.all().update(age=F("age") + 1)

# values_for_update = {'name': 'Bob', 'age': 31}
# bob, created = Person.objects.update_or_create(id=2, defaults=values_for_update)

# f = Person.objects.get(id=1)
# f.name = 'Zora'
# s = Person.objects.get(id=2)
# s.age = 10
# n = Person.objects.bulk_update([f, s], ['name', 'age'])

# Person.objects.all().delete()

# for i in Person.objects.exclude(name='Bob'):
#     print(i.name, i.age)


print(Person.objects.filter(name__iexact='Bob'))
print(Person.objects.filter(name__contains='k'))
print(Person.objects.filter(name__icontains='T'))
print(Person.objects.filter(name__regex=r'(ob|te)$'))
