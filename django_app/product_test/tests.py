from django.test import TestCase
from django.core.urlresolvers import reverse
from product_test.factories import ProductTestFactory


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