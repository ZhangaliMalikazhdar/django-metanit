from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('main')


def products(request):
    return HttpResponse('products')


def new(request):
    return HttpResponse('new product')


def top(request):
    return HttpResponse('popular')
