from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>zero</h1>', content_type='text/plain', charset='utf-8')


def about(request, name, age):
    return HttpResponse(f'''
        <h2>about user</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    ''')


def contact(request):
    return HttpResponse('contact')
