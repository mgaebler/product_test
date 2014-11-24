# coding: utf-8

from django.contrib import messages
from django.views.generic import ListView, RedirectView
from django.views.decorators.cache import never_cache

from django.shortcuts import get_object_or_404, redirect
from simple_bank import models as bank
from . import models


class ShopItemsListView(ListView):
    model = models.Product



@never_cache
def shop_buy_item_view(request, pk):
        item = get_object_or_404(models.Product, pk=pk)
        transfer = bank.create_transfer(
            request.user.bank_account.all().first(),
            bank.Account.objects.get(name='shop'),
            item.value,
            u'Artikel erworben: {}'.format(item.name)
        )
        if transfer.executed:
            messages.info(request, u'Du hast {} erworben.'.format(item.name))
        else:
            messages.info(request, u'Diese Aktion ist nicht möglich.')

        return redirect('user:trendshop')



