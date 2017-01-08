import csv
import os
from django.conf.urls import patterns, url
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from . models import Survey
from . models import SurveyUser


class SurveyUserInline(admin.TabularInline):
    model = SurveyUser
    extra = 0
    readonly_fields = ("user", "uid")


class SurveyAdmin(admin.ModelAdmin):
    inlines = (SurveyUserInline,)

    class Media:
        css = {
            'all': ('admin/css/product-test.css', )
        }

    def add_email_addresses(self, request, survey_id):
        """
        Adds e-mail addresses to umfrage online file
        """
        umfrage_online_file = request.FILES.get("umfrage_online_file")
        if not umfrage_online_file:
            messages.add_message(request, messages.ERROR, "Datei Umfrage ist erforderlich!")
            return redirect(request.META.get("HTTP_REFERER"))

        filename = "{}-emails{}".format(*os.path.splitext(umfrage_online_file.name))
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}".format(filename)
        writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

        for i, row in enumerate(csv.reader(umfrage_online_file, delimiter=';', quotechar='"')):
            if i == 0:
                row.insert(0, 'E-Mail')
            else:
                try:
                    survey_user = SurveyUser.objects.get(survey_id=survey_id, uid=row[2])
                except SurveyUser.DoesNotExist:
                    row.insert(0, "User existiert nicht")
                else:
                    row.insert(0, survey_user.user.email)

            writer.writerow(row)

        return response

    def get_urls(self):
        urls = super(SurveyAdmin, self).get_urls()
        extra_urls = patterns("",
            url("^(?P<survey_id>\d+)/add-email-addresses/$",
                self.admin_site.admin_view(self.add_email_addresses),
                name="add_email_addresses"),
        )
        return extra_urls + urls

admin.site.register(Survey, SurveyAdmin)
