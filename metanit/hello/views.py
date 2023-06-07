from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request, id):
    people = ['Tom', 'Bob', 'Sam']
    if id in range(len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound('nt fnd')


def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest('inc data')
    elif age > 17:
        return HttpResponse('access')
    else:
        return HttpResponseForbidden('not enough age')

# def about(request):
#     return HttpResponse('about')
#
#
# def contact(request):
#     return HttpResponseRedirect('/about')
#
#
# def details(request):
#     return HttpResponsePermanentRedirect('/')


# def user(request):
#     age = request.GET.get('age', 0)
#     name = request.GET.get('name', 'Undefined')
#     return HttpResponse(f'<h2>Name: {name} Age: {age}</h2>')
#
#
# def products(request):
#     return HttpResponse('products')
#
#
# def new(request):
#     return HttpResponse('new product')
#
#
# def top(request):
#     return HttpResponse('popular')
