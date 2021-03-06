# from __future__ import unicode_literals
# from future.builtins import bytes, open

import csv
from mimetypes import guess_type
from os.path import join
from datetime import datetime
from io import BytesIO, StringIO

from django.conf.urls import patterns, url
from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.templatetags.static import static
from django.utils.translation import ungettext, ugettext_lazy as _

from forms_builder.forms.forms import EntriesForm
from forms_builder.forms.models import Form, Field, FormEntry, FieldEntry
from forms_builder.forms.settings import CSV_DELIMITER, UPLOAD_ROOT
from forms_builder.forms.settings import USE_SITES, EDITABLE_SLUGS, CHOICES_QUOTE
from forms_builder.forms.utils import now, slugify

try:
    import xlwt
    XLWT_INSTALLED = True
    XLWT_DATETIME_STYLE = xlwt.easyxf(num_format_str='MM/DD/YYYY HH:MM:SS')
except ImportError:
    XLWT_INSTALLED = False


fs = FileSystemStorage(location=UPLOAD_ROOT)
form_admin_filter_horizontal = ()
form_admin_fieldsets = [
    (None, {"fields": ("title", "slug", ("status",),
        ("publish_date", "expiry_date",),
        "intro", "button_text", "response", "redirect_url", "trendpoints", "image")}),
    (_("Email"), {"fields": ("send_email", "email_from", "email_copies",
        "email_subject", "email_message")}),]


if USE_SITES:
    form_admin_fieldsets.append((_("Sites"), {"fields": ("sites",),
        "classes": ("collapse",)}))
    form_admin_filter_horizontal = ("sites",)


class FieldAdmin(admin.TabularInline):
    model = Field
    exclude = ('slug', )


class FormAdmin(admin.ModelAdmin):
    formentry_model = FormEntry
    fieldentry_model = FieldEntry

    inlines = (FieldAdmin,)
    list_display = ("title", "status", "email_copies", "publish_date",
                    "expiry_date", "total_entries", "position", "admin_links")
    list_display_links = ("title",)
    list_editable = ("status", "email_copies", "publish_date", "expiry_date", "position")
    list_filter = ("status",)
    filter_horizontal = form_admin_filter_horizontal
    search_fields = ("title", "intro", "response", "email_from",
                     "email_copies")
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = form_admin_fieldsets

    class Media:
        js = (
            static('/static/forms/admin_list_reorder.js'),
        )

    def get_queryset(self, request):
        """
        Annotate the queryset with the entries count for use in the
        admin list view.
        """
        qs = super(FormAdmin, self).get_queryset(request)
        return qs.annotate(total_entries=Count("entries"))

    def get_urls(self):
        """
        Add the entries view to urls.
        """
        urls = super(FormAdmin, self).get_urls()
        extra_urls = patterns("",
            url("^(?P<form_id>\d+)/entries/$",
                self.admin_site.admin_view(self.entries_view),
                name="form_entries"),
            url("^(?P<form_id>\d+)/entries/show/$",
                self.admin_site.admin_view(self.entries_view),
                {"show": True}, name="form_entries_show"),
            url("^(?P<form_id>\d+)/entries/export/$",
                self.admin_site.admin_view(self.entries_view),
                {"export": True}, name="form_entries_export"),
            url("^file/(?P<field_entry_id>\d+)/$",
                self.admin_site.admin_view(self.file_view),
                name="form_file"),
        )
        return extra_urls + urls

    def entries_view(self, request, form_id, show=False, export=False,
                     export_xls=False):
        """
        Displays the form entries in a HTML table with option to
        export as CSV file.
        """
        if request.POST.get("back"):
            bits = (self.model._meta.app_label, self.model.__name__.lower())
            change_url = reverse("admin:%s_%s_change" % bits, args=(form_id,))
            return HttpResponseRedirect(change_url)
        form = get_object_or_404(self.model, id=form_id)
        post = request.POST or None
        args = form, request, self.formentry_model, self.fieldentry_model, post
        entries_form = EntriesForm(*args)
        delete = "%s.delete_formentry" % self.formentry_model._meta.app_label
        can_delete_entries = request.user.has_perm(delete)
        submitted = entries_form.is_valid() or show or export or export_xls
        export = export or request.POST.get("export")
        export_xls = export_xls or request.POST.get("export_xls")
        if submitted:
            if export:
                response = HttpResponse(content_type="text/csv")
                response["Content-Disposition"] = "attachment; filename={}.csv".format(form.slug)
                writer = csv.writer(response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)

                title_row = [u"Name", u"E-Mail"]
                for field in form.fields.all():
                    title_row.append(field.label.encode("utf-8"))
                    choices = field.get_choices()
                    if choices:
                        for choice in tuple(choices)[0:-1]:
                            title_row.append(u"")
                writer.writerow(title_row)

                add_title_row_2 = False
                title_row_2 = [u"", u""]
                for field in form.fields.all():
                    if field.choices:
                        add_title_row_2 = True
                        for choice in field.get_choices():
                            title_row_2.append(choice[0].encode("utf-8"))
                    else:
                        title_row_2.append(u"")

                if add_title_row_2:
                    writer.writerow(title_row_2)

                for form_entry in form.entries.all():
                    row = [form_entry.user.full_name.encode("utf-8"), form_entry.user.email.encode("utf-8")]
                    if form_entry.fields.count() == 0:  # user has deleted her entries
                        continue
                    for field in form.fields.all():
                        try:
                            field_entry = FieldEntry.objects.get(entry=form_entry, field_id=field.id)
                        except FieldEntry.DoesNotExist:
                            row.append(u"")
                        else:

                            if field.choices:
                                value = field_entry.value.strip()
                                for choice in field.get_choices():
                                    if value.find(choice[0]) != -1:
                                        row.append(choice[0].encode("utf-8"))
                                    else:
                                        row.append(u"")
                            else:
                                row.append(field_entry.value.encode("utf-8"))
                    writer.writerow(row)
                return response

            elif request.POST.get("delete") and can_delete_entries:
                selected = request.POST.getlist("selected")
                if selected:
                    try:
                        from django.contrib.messages import info
                    except ImportError:
                        def info(request, message, fail_silently=True):
                            request.user.message_set.create(message=message)
                    entries = self.formentry_model.objects.filter(id__in=selected)
                    count = entries.count()
                    if count > 0:
                        entries.delete()
                        message = ungettext("1 entry deleted",
                                            "%(count)s entries deleted", count)
                        info(request, message % {"count": count})
        template = "admin/forms/entries.html"
        context = {"title": _("View Entries"), "entries_form": entries_form,
                   "opts": self.model._meta, "original": form,
                   "can_delete_entries": can_delete_entries,
                   "submitted": submitted,
                   "xlwt_installed": XLWT_INSTALLED}
        return render_to_response(template, context, RequestContext(request))

    def file_view(self, request, field_entry_id):
        """
        Output the file for the requested field entry.
        """
        model = self.fieldentry_model
        field_entry = get_object_or_404(model, id=field_entry_id)
        path = join(fs.location, field_entry.value)
        response = HttpResponse(content_type=guess_type(path)[0])
        f = open(path, "r+b")
        response["Content-Disposition"] = "attachment; filename=%s" % f.name
        response.write(f.read())
        f.close()
        return response


admin.site.register(Form, FormAdmin)
