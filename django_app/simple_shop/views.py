# coding: utf-8

from django.contrib import messages
from django.core.mail import send_mail
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
        user = request.user
        transfer = bank.create_transfer(
            request.user.bank_account.all().first(),
            bank.Account.objects.get(name='shop'),
            item.value,
            u'Artikel erworben: {}'.format(item.name)
        )
        if transfer.executed:
            messages.info(request, u'Du hast {} erworben.'.format(item.name))

            message = u"""
                Artikel:
                - ID: {item_id}
                - Name: {item_name}
                - Value: {item_value}

                User:
                - Name: {user_name}
                - Adress:
                    {user_address1}
                    {user_address2}
                    {user_address3}
            """.format(
                item_id=item.id,
                item_name=item.name,
                item_value=item.value,
                user_name=user.full_name,
                user_address1=user.address1,
                user_address2=user.address2,
                user_address3=user.address3,
            )

            send_mail(
                u'Trendpoints eingelöst',
                message,
                'info@trendsetter.eu',
                ['info@trendsetter.eu']
            )
        else:
            messages.info(request, u'Diese Aktion ist nicht möglich.')

        return redirect('user:trendshop')



