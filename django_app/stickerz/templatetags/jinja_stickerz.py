# coding: utf-8
from __future__ import absolute_import
import logging
from django import template
from django.template.loader import get_template
from django.template import Context
from django_jinja import library
from stickerz.models import StickerContainer
from django.utils.timezone import utc


log = logging.getLogger(__name__)

register = template.Library()



@library.global_function
def stickers(identifier=""):
    try:
        container = StickerContainer.objects.get(
            identifier=identifier,
            active=True
        )

        template_path = "stickerz/base.jinja" if not container.template else container.template
        template = get_template(template_path)
        context = Context({ "stickers": container.stickers.all() })

        return template.render(context)

    except StickerContainer.DoesNotExist:
        log.warning('Cannot find the sticker container ')


