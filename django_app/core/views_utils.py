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
