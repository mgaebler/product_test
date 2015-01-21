# coding: utf-8
import factory
from faq import models


class FaqGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.FaqGroup
    name = factory.Sequence(lambda n: "Test Faq #%s" % n)
    text = custom_html = """
        This headline
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
    """


class FaqEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.FaqEntry
    question = factory.Sequence(lambda n: "Test Question #%s" % n)
    answer = factory.Sequence(lambda n: "Test Answer #%s" % n)
    group = factory.SubFactory(FaqGroupFactory)
    position = factory.Sequence(lambda n: n)