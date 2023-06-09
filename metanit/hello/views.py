from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseRedirect, HttpResponsePermanentRedirect, \
    JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    bob = Person('Bob', 32)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return {'name': o.name, 'age': o.age}
            # return o.__dict__
        return super().default(o)
    

# def access(request, age):
#     if age not in range(1, 111):
#         return HttpResponseBadRequest('inc data')
#     elif age > 17:
#         return HttpResponse('access')
#     else:
#         return HttpResponseForbidden('not enough age')

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
