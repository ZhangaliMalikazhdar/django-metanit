from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'company']


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    fields = ['name']


class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'courses']


admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
