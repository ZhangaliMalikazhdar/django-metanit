from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseRedirect, HttpResponsePermanentRedirect, \
    JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.template.response import TemplateResponse


# set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)
# set_signed_cookie(key, value, salt='', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)
# get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)

def set(request):
    username = request.GET.get('username', 'Undefin')
    response = HttpResponse(f'Helo {username}')
    response.set_cookie('username', username)
    return response


def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f'helo {username}')


def index(request):
    data = {'header': 'hola dj', 'message': 'welcome to py'}
    header = 'data user'
    langs = ['python', 'java', 'csharp']
    user = {'name': 'Tom', 'age': 23}
    address = ('Abrik', 23, 34)
    dzz = {'header': header, 'langs': langs, 'user': user, 'address': address}
    return TemplateResponse(request, 'index.html', context=dzz)
    # bob = Person('Bob', 32)
    # return JsonResponse(bob, safe=False, encoder=PersonEncoder)


def zzz(request):
    print(Person('Tom').name)
    return render(request, 'zzz.html', context={'person': Person('Tom')})


class Person:
    def __init__(self, name, age=0):
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
