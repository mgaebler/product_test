# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment


admin.site.register(Comment)
