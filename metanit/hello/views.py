from .models import Person
from django.db.models import Avg, Min, Max, Sum


people = Person.objects.order_by('-name', 'age')
for person in people:
    print(person)
print()

# people = Person.objects.values('name')
# people = Person.objects.values_list()
# people = Person.objects.values_list('name', flat=True)
people = Person.objects.values_list('name', flat=True).distinct()
print(people)
print()

bob = Person.objects.filter(name='Bob')
akame = Person.objects.filter(name='Akame')
print(akame.union(bob, all=False).values())
# union intersection difference
print()

print(Person.objects.latest('id').id)
print(Person.objects.earliest('-id').id)

print(Person.objects.first())
print(Person.objects.last())
print()

print(Person.objects.filter(age__gt=134).exists())
print(Person.objects.filter(age__gte=10).contains(Person.objects.last()))
print()

print(Person.objects.acount())
# Что использовать: count или len? Если объекты уже ранее были загружены (например, с помощью метода all()), то оптимальнее использовать функцию len(), которая не выполняет к базе данных запрос SQL, а работает с уже загруженным набором объектов. Если же объекты ранее НЕ были загружены, то лучше выполнить метод count(), для которого не потребуется загружать все объекты из бд.
print(Person.objects.aggregate(Avg('age')))
print(Person.objects.aggregate(Sum('age')))
print(Person.objects.aggregate(Min('age')))
print(Person.objects.aggregate(Max('age')))
