# coding: utf-8
from __future__ import unicode_literals
import csv
import logging
from django.conf.urls import patterns, url
from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.templatetags.static import static
from .models import ProductTest, Brand, Participation, TestResult
from simple_bank.models import Account
from simple_bank.models import create_transfer 
from surveys.models import SurveyUser

logger = logging.getLogger(__name__)


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1
    raw_id_fields = ('users',)


@admin.register(ProductTest)
class ProductTestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at',)
    inlines = (ParticipationInline,)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'brand')
        },),
        ('Images', {
            'fields': (
                ('hero_image', 'hero_image_url',),
                ('list_image', 'list_image_url',),
                ('logo', 'logo_url',),
            )
        }),
        ('Surveys', {
            'fields': (
                ('application_survey', 'application_survey_start', 'application_survey_end'),
                ('completion_survey', 'completion_survey_start', 'completion_survey_end'),
            )
        }),
        ('Customization', {
            'fields': ('custom_html', 'custom_css',)
        }),
        ('Additional Pages', {
            'fields': ('gallery', 'faq', 'forum', 'test_result')
        }),
        (None, {
            'fields': (
                'published_at',
                'activated_at',
                'ends_at',
                'state',
                ('updated_at', 'created_at',),
            )
        })
    )

    class Media:
        js = [
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            static('product_test/tinymce_setup/tinymce_setup.js'),
        ]

    def upload_trendpoints(self, request, product_test_id):
        """
        View to add trendpoints via upload a csv file.
        """
        # TOOD: Use Django Form?
        try:
            product_test = ProductTest.objects.get(pk=product_test_id)
        except ProductTest.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Produkttest existiert nicht mehr!")
            return redirect(request.META.get("HTTP_REFERER"))

        trendpoints_file = request.FILES.get("trendpoints_file")
        if not trendpoints_file:
            messages.add_message(request, messages.ERROR, "Datei ist erforderlich!")

        trendpoints = request.POST.get("trendpoints")
        if not trendpoints:
            messages.add_message(request, messages.ERROR, "Trendpoints sind erforderlich!")
        try:
            trendpoints = int(trendpoints)
        except (ValueError, TypeError):
            messages.add_message(request, messages.ERROR, "Trendpoints muss Zahl sein!")
            trendpoints = 0
            
        reference = request.POST.get("reference")
        if not reference:
            messages.add_message(request, messages.ERROR, "Referenz ist erforderlich!")

        if not (trendpoints_file and trendpoints and reference):
            return redirect(request.META.get("HTTP_REFERER"))

        created = False
        for row in csv.reader(trendpoints_file, delimiter=str(';'), quotechar=str('"')):
            try:
                survey = product_test.completion_survey
                survey_user = SurveyUser.objects.get(
                    survey=survey,
                    uid=row[0],
                )
            except SurveyUser.DoesNotExist:
                logger.info(u"User does not exist for survey '{}' and uid '{}'".format(survey.id, row[0]))
            else:
                sender = Account.objects.get(name="trendsetter")

                try:
                    receiver = Account.objects.get(customer__email=survey_user.user.email)
                except Account.DoesNotExist:
                    logger.info(u"User {} does not have a bank account".format(survey.user.email))
                else:
                    created = True
                    create_transfer(
                        sender_account=sender,
                        receiver_account=receiver,
                        amount=trendpoints,
                        message=reference,
                    )
                    logger.info(u"Added {} to account {} by upload".format(trendpoints, sender.name))
        if created:
            messages.add_message(request, messages.INFO, "Trendpoints wurden hinzugefügt.")
        else:
            messages.add_message(request, messages.WARNING, "Es wurden keine Trendpoints hinzugefügt.")

        return redirect(request.META.get("HTTP_REFERER"))

    def upload_particpations(self, request, product_test_id):
        """
        View to add participation via upload a csv file.
        """
        try:
            product_test = ProductTest.objects.get(pk=product_test_id)
        except ProductTest.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Produkttest existiert nicht mehr!")
            return redirect(request.META.get("HTTP_REFERER"))

        participations = request.FILES.get("participations")
        if not participations:
            messages.add_message(request, messages.ERROR, "Datei ist erforderlich!")
            return redirect(request.META.get("HTTP_REFERER"))

        created = False
        for row in csv.reader(participations, delimiter=str(';'), quotechar=str('"')):
            try:
                survey = product_test.application_survey
                survey_user = SurveyUser.objects.get(
                    survey=survey,
                    uid=row[0],
                )
            except SurveyUser.DoesNotExist:
                logger.info(u"User does not exist for survey '{}' and uid '{}'".format(survey.id, row[0]))
            else:
                created = True
                Participation.objects.get_or_create(
                    users=survey_user.user,
                    product_test=product_test
                )

        if created:
            messages.add_message(request, messages.INFO, "Participations wurden hinzugefügt.")
        else:
            messages.add_message(request, messages.WARNING, "Es wurden keine Participations hinzugefügt.")

        return redirect(request.META.get("HTTP_REFERER"))

    def get_urls(self):
        """
        Add the upload particpations view to urls.
        """
        urls = super(ProductTestAdmin, self).get_urls()
        extra_urls = patterns("",
            url("^(?P<product_test_id>\d+)/upload-trendpoints/$",
                self.admin_site.admin_view(self.upload_trendpoints),
                name="upload_trendpoints"),
            url("^(?P<product_test_id>\d+)/upload-particpations/$",
                self.admin_site.admin_view(self.upload_particpations),
                name="upload_particpations"),
        )
        return extra_urls + urls


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    class Media:
        js = [
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            static('grappelli/tinymce_setup/tinymce_setup.js'),
        ]


admin.site.register(Brand)
