from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Products(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    photo = ThumbnailerImageField()
    value = models.IntegerField()

    def __unicode__(self):
        return self.name