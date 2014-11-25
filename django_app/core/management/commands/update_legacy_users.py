# coding: utf-8
import json
from django.core.management.base import BaseCommand, CommandError
from user_accounts.models import UserAccount
from simple_bank import models

users = json.load(open('import/users.json'))


class Command(BaseCommand):
    help = 'Import legacy users'

    def handle(self, *args, **options):
        count = 0

        for user in users:
            self.stdout.write(u"Import:{} - {}".format(count, user.get('email')))
            # check if user exists
            if UserAccount.objects.filter(email=user.get('email')).exists():
                u = UserAccount.objects.get(email=user.get('email'))

                if user.get('confirmed_at'):
                    u.confirmation_at=user.get('confirmed_at')

                    u.save()
                    count +=1
