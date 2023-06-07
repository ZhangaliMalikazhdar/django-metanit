from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('main')


def user(request):
    age = request.GET.get('age', 0)
    name = request.GET.get('name', 'Undefined')
    return HttpResponse(f'<h2>Name: {name} Age: {age}</h2>')


def products(request):
    return HttpResponse('products')


def new(request):
    return HttpResponse('new product')


def top(request):
    return HttpResponse('popular')
