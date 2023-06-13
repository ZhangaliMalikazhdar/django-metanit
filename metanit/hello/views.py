from .models import *


tom = Student.objects.create(name='Tom')
tom.courses.create(name='Algebra')
# courses = Student.objects.get(name='Tom').courses.all()

students = Student.objects.filter(courses__name='Algebra')
print(students.values_list)
python = Course.objects.create(name='Python')
python.student_set.create(name='Bob')

sam = Student(name='Sam')
sam.save()
python.student_set.add(sam)

students = python.student_set.all()

number = python.student_set.count()

python.student_set.remove(sam)

python.student_set.clear()
