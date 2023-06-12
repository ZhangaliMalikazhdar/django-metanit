from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')


def edit(request, pk):
    try:
        person = Person.objects.get(id=pk)

        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Prs nt found</h2>')


def delete(request, pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>prs nt fnd')
