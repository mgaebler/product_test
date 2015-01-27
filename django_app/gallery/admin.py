from django.contrib import admin
from gallery.models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = (GalleryImageInline,)

admin.site.register(GalleryImage)


