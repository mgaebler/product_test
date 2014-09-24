from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import ProductTest


class ProductTestList(ListView):
    model = ProductTest
    context_object_name = "product_test_list"


class ProductTestDetail(DetailView):
    model = ProductTest
    context_object_name = 'product_test'
