from .models import Person


people = Person.objects.all()
print(people.query)

people = people.filter(name='Tom')
print(people.query)

people = people.filter(age=31)
print(people.query)

for person in people:
    print(f'{person.id}.{person.name} - {person.age}')
