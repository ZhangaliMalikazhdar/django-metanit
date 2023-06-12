from .models import Person
from django.db import connection


people = Person.objects.raw('SELECT id, name from hello_person')
for person in people:
    print(person)
print(people[1].name)
print()
print(Person.objects.filter(age__lte=40).raw('select * from hello_person')[0])
# nothing matter
print()

name = 'Bob'
age = 30
people = Person.objects.raw('select * from hello_person where name = %s or age > %s', [name, age])
for i in people:
    print(i)
print()

# with connection.cursor() as cursor:
#     cursor.execute('update hello_person set name="Tomas" where name="Bob" and age=10')
#     cursor.execute('select * from hello_person')
#     row = cursor.fetchone()
#     print(row)

# z = Person.objects.values_list()
# print(z)

old = 'Tomas'
new = 'Tom'
with connection.cursor() as cursor:
    cursor.execute('update hello_person set name = %s where name = %s', [new, old])
    cursor.execute('select * from hello_person where name="Tom"')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
