from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2>main</h2>')


def user(request, name, age):
    return HttpResponse(f'<h2>Name: {name}, {age}</h2>')


def about(request, name, age):
    return HttpResponse(f'''
        <h2>about user</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    ''')


def contact(request):
    return HttpResponse('contact')
