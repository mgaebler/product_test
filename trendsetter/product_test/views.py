from django.shortcuts import render
from django.views.generic import DetailView
from .models import ProductTest


class ProductTestDetail(DetailView):
    model = ProductTest
    context_object_name = 'product_test'
