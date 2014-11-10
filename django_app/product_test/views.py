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


class ProductBrandDetailView(DetailView):
    template_name = 'product_test/brand_detail.jinja'
    model = Brand
    context_object_name = 'brand'


class ProductBrandListView(ListView):
    template_name = 'product_test/brand_list.jinja'
    model = Brand
    context_object_name = 'brands'


# form view


# gallery view
class GalleryView(ProductTestDetail):
    template_name = 'product_test/gallery.jinja'
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['image_upload_form'] = ImageUploadForm()
        context['video_upload_form'] = VideoLinkUploadForm()
        return context

# test result view
