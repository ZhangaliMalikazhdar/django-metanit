from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse(f'<h2>hola, {name}')
        else:
            return HttpResponse('Inv data')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})


def postuser(request):
    name = request.POST.get('name', 'Undefin')
    age = request.POST.get('age', 1)
    langs = request.POST.getlist('languages', ['python'])
    return HttpResponse(f'''
        <div>Name: {name} Age: {age}</div>
        <div>Languages: {langs}</div>
        ''')
