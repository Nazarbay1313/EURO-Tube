from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from myapp.models import Product, Tag


class HomeViewTestCase(TestCase):
    fixtures = ['products.json', 'tags.json']

    def setUp(self):
        self.products = Product.objects.all()
        self.tags = Tag.objects.first()

    def test_list(self):
        path = reverse('home')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(list(response.context_data['products']), list(self.products[:3]))

    def test_tags(self):
        path = reverse('tags', kwargs={'tag_slug': self.tags.slug})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']),
                         list(self.products.filter(tags__slug=self.tags.slug)))

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'product/index.html')
        self.assertEqual(response.context_data['title'], 'STORE - Каталог')
