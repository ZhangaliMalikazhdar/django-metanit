"""
URL configuration for metanit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from hello import views

# product_patterns = [
#     path('', views.products),
#     path('new', views.new),
#     path('top', views.top),
# ]

urlpatterns = [
    path('index/<int:id>', views.index),
    path('access/<int:age>', views.access),

    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('details/', views.details),

    # path('user/', views.user),
    # path('products/', include(product_patterns)),
]
