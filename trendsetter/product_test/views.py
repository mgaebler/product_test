from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import ProductTest, Brand


class ProductTestList(ListView):
    model = ProductTest
    context_object_name = "product_test_list"


class ProductTestDetail(DetailView):
    model = ProductTest
    context_object_name = 'product_test'


class ProductBrandDetailView(DetailView):
    template_name = 'product_test/brand_detail.jinja'
    model = Brand
    context_object_name = 'brand'


class ProductBrandListView(ListView):
    template_name = 'product_test/brand_list.jinja'
    model = Brand
    context_object_name = 'brands'