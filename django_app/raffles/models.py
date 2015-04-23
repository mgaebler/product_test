from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from senseo.models import SEOData
from simple_comments.models import Comment


class StartedRaffleManager(models.Manager):
    def started(self):
        """
        Returns only raffles which have a start date and the start date is in
        past.
        """
        qs = super(StartedRaffleManager, self).get_queryset()
        return qs.filter(starts_at__lte=timezone.now())


class Raffle(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'), default=False)
    logo = models.ImageField(_('Logo'), upload_to="raffles", blank=True, null=True)
    list_image = models.ImageField(_('List Image'), upload_to="raffles", blank=True, null=True)
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    comments = GenericRelation(Comment)
    seo_data = GenericRelation(SEOData)

    objects = StartedRaffleManager()

    class Meta:
        verbose_name = _('raffle')
        verbose_name_plural = _('raffles')
        ordering = ('starts_at', 'ends_at')

    def __unicode__(self):
        return "%s -- %s" % (self.url, self.title)

    def is_expired(self):
        """
        Raffle is expired if there is an end date and the end date is in past.
        """
        return self.ends_at and (self.ends_at < timezone.now())

    def get_absolute_url(self):
        return reverse("raffles:detail", kwargs={"url": self.url})
