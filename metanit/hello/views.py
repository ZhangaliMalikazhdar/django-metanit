from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def postuser(request):
    name = request.POST.get('name', 'Undefin')
    age = request.POST.get('age', 1)
    langs = request.POST.getlist('languages', ['python'])
    return HttpResponse(f'''
        <div>Name: {name} Age: {age}</div>
        <div>Languages: {langs}</div>
        ''')
