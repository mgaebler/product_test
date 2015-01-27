# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class StickerContainer(models.Model):
    """
    Containers hold their stickers. They know about the place they live and the template they use.
    """
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=24)
    description = models.TextField(help_text=_("Say something about this container. For example where it lives."))
    active = models.BooleanField(verbose_name=_('active'), default=True)
    template = models.CharField(max_length=255, blank=True, null=True,
                                help_text='Optional: A template corresponding to your container format.')
    def __unicode__(self):
        return u'{0}'.format(self.name)


class Sticker(models.Model):
    name = models.CharField(_('name'), max_length=250)
    target_url = models.URLField(max_length=510, blank=True, null=True)
    container = models.ForeignKey(StickerContainer, related_name=('stickers'))
    image = models.ImageField(upload_to='stickerz')
    position = models.PositiveSmallIntegerField()

    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modification_date = models.DateTimeField(_('modification_date'), auto_now=True, editable=False)

    def __unicode__(self):
        return "{0}({1})".format(self.name, self.container)

    class Meta:
        ordering = ['position']