# coding: utf-8

from django.views.generic import ListView
from . import models


class ShopItemsListView(ListView):
    model = models.Product
