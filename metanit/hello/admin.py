from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'company']


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
