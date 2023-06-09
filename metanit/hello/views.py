from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={'body': '<h1>helo</h1>'})


def zzz(request):
    return render(request, 'zzz.html')
