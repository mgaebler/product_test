from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Products(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    photo = ThumbnailerImageField()
    value = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name