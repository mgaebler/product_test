from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from product_test.models import ProductTest, Brand
from gallery.forms import ImageUploadForm, VideoLinkUploadForm

class ProductTestList(ListView):
    model = ProductTest
    context_object_name = "product_test_list"


class ProductTestDetail(DetailView):
    model = ProductTest
    context_object_name = 'product_test'

    def get_context_data(self, **kwargs):
        context = super(ProductTestDetail, self).get_context_data(**kwargs)
        product_test = self.get_object()
        if product_test.test_result and product_test.test_result.is_active == True:
            context['test_result'] = product_test.test_result
        return context


class ProductBrandDetailView(DetailView):
    template_name = 'product_test/brand_detail.jinja'
    model = Brand
    context_object_name = 'brand'


class ProductBrandListView(ListView):
    template_name = 'product_test/brand_list.jinja'
    model = Brand
    context_object_name = 'brands'


# test result view
class ResultView(ProductTestDetail):
    template_name = 'product_test/test_result.jinja'
    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['test_result'] = self.get_object().test_result
        return context