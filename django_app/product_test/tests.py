from django.test import TestCase
from django.core.urlresolvers import reverse
from product_test.factories import ProductTestFactory
from faq.factories import FaqEntryFactory

class ProductListPageTestCase(TestCase):
    def setUp(self):
        self.product_test = ProductTestFactory()
        self.list_url = reverse('product_test:index')

    def test_the_title_appears_in_list_view(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.product_test.title)

    # product tests that are not active should not appear in the list


class ProductTestPageTestCase(TestCase):
    def setUp(self):
        self.product_test = ProductTestFactory()
        self.info_url = reverse('product_test:info', kwargs={'slug': self.product_test.slug})

    def test_the_title_appears_in_info_view(self):
        response = self.client.get(self.info_url)
        self.assertContains(response, self.product_test.title)

    def test_faq_entries_appear(self):
        faq = self.product_test.faq
        # add some entries
        entry = FaqEntryFactory.create(group=faq)
        faq_url = reverse('product_test:faq', kwargs={'slug': self.product_test.slug})
        response = self.client.get(faq_url)
        self.assertContains(response, entry.question)
        self.assertContains(response, entry.answer)