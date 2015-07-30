# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import redirect

from product_test.models import ProductTest
from product_test.views import ProductTestDetail

from gallery.forms import ImageUploadForm
from gallery.forms import VideoLinkUploadForm
from gallery.models import GalleryImage


class GalleryView(ProductTestDetail):
    template_name = 'product_test/gallery.jinja'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['gallery'] = self.get_object().gallery
        context['image_upload_form'] = ImageUploadForm()
        context['video_upload_form'] = VideoLinkUploadForm()

        return context


def image_upload_view(request, slug):
    product_test = ProductTest.objects.get(slug=slug)
    if request.method == 'POST':
        gallery = product_test.gallery
        image_upload_form = ImageUploadForm(request.POST, request.FILES)

        if image_upload_form.is_valid():
            image = GalleryImage()
            image.file = image_upload_form.cleaned_data['image']
            image.owner = request.user
            image.gallery = gallery
            image.save()

            messages.info(request, 'Dein Bild wurde erfolgreich gespeichert.')
        else:
            messages.error(request, 'Dein Bild konnte nicht gespeichert werden.')

    return redirect(reverse('product_test:gallery:index', kwargs={'slug': product_test.slug}))


def video_upload_view(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def delete_image(request, slug, image_id):
    try:
        GalleryImage.objects.get(id=image_id).delete()
    except GalleryImage.DoesNotExist:
        pass
    return HttpResponse("ok")
