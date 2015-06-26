# coding=utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from user_accounts.models import UserAccount


class Survey(models.Model):
    """
    Holds all information, which are needed for the integration of online
    suverys based on https://www.umfrageonline.com.
    """
    title = models.CharField(_(u"Titel"), max_length=50)
    url = models.URLField(
        _(u"URL"),
        help_text=_(u"""Die URL der Online-Umfrage, wie diese bei https://www.umfrageonline.com
                     unter 'Umfrage bearbeiten' angezeigt wird. Z.B.: https://www.umfrageonline.com/s/92b3289"""))
    users = models.ManyToManyField(UserAccount, _(u"Gültige Benutzer für diese Umfrage"), through="SurveyUser", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return "{} / {}".format(self.title, self.url)

    def takes_part_in(self, user):
        """
        Returns True if the passed user takes part in this survey.
        """
        return user in self.users.all()


class SurveyUser(models.Model):
    """
    All users need a unique ID per survey. This models holds it.
    """
    user = models.ForeignKey(UserAccount)
    survey = models.ForeignKey(Survey)
    uid = models.CharField(_(u"Eindeutige ID"), max_length=50, blank=True, unique=True)
