from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Product(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField()
    description = models.TextField()
    image = ThumbnailerImageField(upload_to='shop')
    value = models.IntegerField()
    active = models.BooleanField(default=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name