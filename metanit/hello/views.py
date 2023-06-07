from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('haol', headers={"Secret": "o2i3q4u02"})


def about(request, name, age):
    return HttpResponse(f'''
        <h2>about user</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    ''')


def contact(request):
    return HttpResponse('contact')
