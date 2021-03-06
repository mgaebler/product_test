from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns("forms_builder.forms.views",
    url(r"(?P<slug>.*)/sent/$", "form_sent", name="form_sent"),
    url(r"delete-form/(?P<slug>.*)", "delete_form", name="form_delete"),
    # url(r"(?P<slug>.*)/$", "form_detail", name="form_detail"),
)
