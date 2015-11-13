# coding: utf-8
from __future__ import unicode_literals

import datetime
import logging
import pytz

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_simple_forum.models import Forum
from faq.models import FaqGroup
from gallery.models import Gallery
from surveys.models import Survey

log = logging.getLogger('product_test')


class Brand(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, db_index=True)
    url = models.URLField()
    logo = models.ImageField(_(u"Logo overview"))
    logo_top = models.ImageField(blank=True, null=True, help_text=u"""
        When this logo is given, the default trendsetter logo on top left of the
        page is exchanged with this one on all product test pages."""
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.CharField(_(u"Color"), max_length=6, default="fd7263")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'slug': self.slug})


class TestResult(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __unicode__(self):
        return self.title


class ProductTest(models.Model):
    STATE_DRAFT = 'draft'
    STATE_PUBLISHED = 'published'
    STATE_PREVIEW = 'preview'
    STATES = (
        (STATE_DRAFT, _(u'draft')),
        (STATE_PUBLISHED, _(u'published')),
        (STATE_PREVIEW, _(u'preview')),
    )

    slug = models.SlugField(max_length=254, db_index=True)
    title = models.CharField(max_length=254)
    link = models.URLField(max_length=254)
    brand = models.ForeignKey(Brand, null=True, blank=True)
    # Images
    hero_image = models.ImageField(null=True, blank=True)
    hero_image_url = models.URLField(null=True, blank=True)
    list_image = models.ImageField(null=True, blank=True)
    list_image_url = models.URLField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    # Customization
    custom_html = models.TextField(null=True, blank=True)
    custom_css = models.TextField(null=True, blank=True)

    state = models.CharField(max_length=16, choices=STATES, default=u'draft',
        help_text=u"""
            Draft: The product test is not visible to everyone.
            Published: The Product test is visible if the 'published at' date is arrived.
            Preview: The Product is visible to every staff member independently of the 'publishing at' date.
        """
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    activated_at = models.DateTimeField(default=timezone.now, null=True)

    # sub
    faq = models.OneToOneField(FaqGroup, null=True, blank=True)
    gallery = models.OneToOneField(Gallery, null=True, blank=True)
    forum = models.OneToOneField(Forum, null=True, blank=True)
    test_result = models.OneToOneField(TestResult, null=True, blank=True)

    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Participation")

    application_survey = models.ForeignKey(Survey, null=True, blank=True, related_name="application_survey")
    application_survey_start = models.DateTimeField(null=True, blank=True)
    application_survey_end = models.DateTimeField(null=True, blank=True)
    completion_survey = models.ForeignKey(Survey, null=True, blank=True, related_name="completion_survey")
    completion_survey_start = models.DateTimeField(null=True, blank=True)
    completion_survey_end = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_test:info', kwargs={'slug': self.slug})

    def display_application_survey(self, user):
        if self.application_survey and user.is_superuser:
            return True

        now = datetime.datetime.now(pytz.UTC)
        if self.application_survey and \
           self.application_survey_start and \
           self.application_survey_end and \
           (self.application_survey_start < now) and \
           (self.application_survey_end > now):
            return True

        return False

    def takes_part_in(self, user):
        """
        Returns True if passed user participates on the product test.
        """
        if user.is_anonymous():
            return False
        else:
            try:
                Participation.objects.get(
                    users=user,
                    product_test=self,
                )
            except Participation.DoesNotExist:
                return False
            else:
                return True

    def display_completion_survey(self, user):
        if self.completion_survey and user.is_superuser:
            return True

        now = datetime.datetime.now(pytz.UTC)
        if self.completion_survey and \
           self.completion_survey_start and \
           self.completion_survey_end and \
           (self.completion_survey_start < now) and \
           (self.completion_survey_end > now) and \
           self.takes_part_in(user):
            return True

        return False

    def get_detail_link(self, user):
        """
        Returns the detail link for a test for the test overview.
        """
        if self.display_completion_survey(user):
            return reverse("product_test:surveys:completion", kwargs={'slug': self.slug})

        if self.display_application_survey(user):
            return reverse("product_test:surveys:application", kwargs={'slug': self.slug})

        if self.test_result:
            return reverse("product_test:result", kwargs={'slug': self.slug})

        return reverse("product_test:info", kwargs={'slug': self.slug})


class Participation(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL)
    product_test = models.ForeignKey(ProductTest)
    created_at = models.DateTimeField(auto_now_add=True)



def create_product_test_add_ons(sender, **kwargs):
    # use the user instance to create a new account if it not already exists
    product_test = kwargs.get('instance', None)
    if not product_test.faq:
        product_test.faq = FaqGroup.objects.create(
            name=u"{name}-faq".format(name=product_test.title),
            text=u" "
        )
        product_test.save()

    if not product_test.gallery:
        product_test.gallery = Gallery.objects.create(name=u"{name}-gallery".format(name=product_test.title))
        product_test.save()

    if not product_test.forum:
        product_test.forum = Forum.objects.create(title=u"{name}-forum".format(name=product_test.title))
        product_test.save()
    # import pudb; pu.db


post_save.connect(create_product_test_add_ons, sender=ProductTest, dispatch_uid="create_product_test_subs")
