from django.contrib import admin
from .models import ProductTest, Brand


@admin.register(ProductTest)
class ProductTestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'brand')
        },),
        ('Images', {
            'fields': (
                ('hero_image', 'hero_image_url',),
                ('list_image', 'list_image_url',),
                ('logo', 'logo_url',),
            )
        }),
        ('Customization', {
            'fields': ('custom_html', 'custom_css',)
        }),
        (None, {
            'fields': (
                'published_at',
                'activated_at',
                'state',
                ('updated_at', 'created_at',),
            )
        })
    )


admin.site.register(Brand)