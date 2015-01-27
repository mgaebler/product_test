# coding: utf-8
from django_jinja import library
from django.utils import timezone


@library.global_function
def now():
    return timezone.now()