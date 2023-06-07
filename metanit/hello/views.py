from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'''
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    ''')


def about(request, name, age):
    return HttpResponse(f'''
        <h2>about user</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    ''')


def contact(request):
    return HttpResponse('contact')
