# coding: utf-8
import csv
from django.contrib.admin.views.decorators import staff_member_required
from django.http import StreamingHttpResponse
from user_accounts.models import UserAccount


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


@staff_member_required
def streaming_csv_view(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = ([user.email] for user in UserAccount.objects.exclude(confirmation_at=None))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="confirmed_users.csv"'
    return response


@staff_member_required
def get_gender_birth_date_csv(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = ([user.gender, user.birth_date] for user in UserAccount.objects.all())
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="gender_birthdate_list.csv"'
    return response


@staff_member_required
def all_users_csv_view(request):
    """A view that streams a large CSV file of all users."""

    rows = [[
        u"Nutzername",
        u"E-Mail",
        u"Name",
        u"Aktiv",
        u"Geschlecht",
        u"Familienstand",
        u"Adresse",
        u"PLZ",
        u"Stadt",
        u"Land",
        u"Geburtsdatum",
    ]]

    for user in UserAccount.objects.all():
        address = user.address1
        if user.address2:
            address += u" / " + user.address2
        if user.address3:
            address += u" / " + user.address3

        row = []
        for field in [
            user.preferred_name,
            user.email,
            user.full_name,
            user.is_active,
            user.gender,
            user.family_status,
            address,
            user.postcode,
            user.city,
            user.country,
            user.birth_date,
        ]:
            # csv module doesn't support Unicode input
            try:
                field = field.encode("utf-8")
            except AttributeError:
                pass
            row.append(field)

        rows.append(row)

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    return response
