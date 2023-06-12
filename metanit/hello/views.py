from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponseNotFound


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def create(request):
    create_companies()

    if request.method == 'POST':
        product = Product()
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.company_id = request.POST.get('company')
        product.save()
        return HttpResponseRedirect('/')

    companies = Company.objects.all()
    return render(request, 'create.html', {'companies': companies})


def edit(request, pk):
    try:
        product = Product.objects.get(id=pk)

        if request.method == 'POST':
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.company_id = request.POST.get('company')
            product.save()
            return HttpResponseRedirect('/')
        else:
            companies = Company.objects.all()
            return render(request, 'edit.html', {'product': product, 'companies': companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>pr nt fnd</h2>')


def delete(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2> pr nt f</h2>')


def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name='Apple')
        Company.objects.create(name='Asus')
        Company.objects.create(name='MSI')
