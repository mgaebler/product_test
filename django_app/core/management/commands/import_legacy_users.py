# coding: utf-8
import json
from django.core.management.base import BaseCommand, CommandError
from user_accounts.models import UserAccount

users = json.load(open('users.json'))


class Command(BaseCommand):
    help = 'Import legacy users'

    def handle(self, *args, **options):
        count = 0
        for user in users:
            self.stdout.write(u"Import:{} - {}".format(count, user.get('email')))
            # check if user exists
            if UserAccount.objects.filter(email=user.get('email')).exists():
                u = UserAccount.objects.get(email=user.get('email'))
            else:
                u = UserAccount.objects.create_user(user.get('email').strip())
            # u.legacy_id=int(user.get('id'))
            if user.get('name'):
                u.full_name=user.get('name')

            if user.get('nickname'):
                u.preferred_name=user.get('nickname')

            if user.get('city'):
                u.city=user.get('city')

            if user.get('address1'):
                u.address1=user.get('address1')

            u.address2=user.get('address2')
            u.address3=user.get('address3')

            if user.get('postcode'):
                if not len(user.get('postcode')) > 12:
                    u.postcode=user.get('postcode')
            # user['invited_by']

            if user.get('status') == 'single':
                u.family_status='si'
            elif user.get('status') == 'with-partner':
                u.family_status='pa'
            elif user.get('status') == 'married':
                u.family_status='ma'
            elif user.get('status') == 'divorced':
                u.family_status='di'
            elif user.get('status') == 'other':
                u.family_status='an'

            if user.get('gender'):
                u.gender=user.get('gender')
            # u.birth_date=user.get('birthdate')
            # u.avatar=user['avatar']
            if user.get('country'):
                u.country=user.get('country')

            u.save()
            count +=1


user = {
    u'confirmed_at': u'2014-04-29 14:33:23',
    u'updated_at': u'2014-07-03 09:59:32',
    u'referral_token': u'W5O3_D1t6ZZQqR1m1-MOcA',
    u'postcode': u'22769',
    u'id': u'1',
    u'city': u'Hamburg',
    u'trendpoints': u'25',
    u'email': u'matthias.bauer@intosite.de',
    u'status': u'other',
    u'recovery_token': None,
    u'address1': u'Stresemannstra\xdfe 71',
    u'address2': u'',
    u'address3': u'',
    u'invited_by': None,
    u'password_digest': u'$2a$10$TlgFKoy5owXU/ol1QF2xuOFDNeVAg.ghLVEoxkHw5L4RpWFD4N0au',
    u'nickname': u'matthias.bauer',
    u'confirmation_token': u'a_i7zfT3bjMm9BF742J7nA',
    u'name': u'Matthias Bauer',
    u'gender': u'o',
    u'created_at': u'2014-04-29 14:27:49',
    u'birthdate': u'1983-05-01',
    u'avatar_url': None,
    u'avatar': u'm_ava_v3_1x1_lr.jpg',
    u'country': u'de'
}

