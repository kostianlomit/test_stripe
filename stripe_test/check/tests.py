from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

from .models import Item


# Test models
class ItemTestCase(TestCase):

    def setUp(self):
        Item.objects.create(id="1", name="first", description="ffff", prise=100)

    def test_stripe_name(self):
        first = Item.objects.get(id=1)
        field_label = first._meta.get_field('first').verbose_name
        self.assertEquals(field_label, 'first')

    def test_first_name_max_length(self):
        author = Item.objects.get(id=1)
        max_length = author._meta.get_field('first').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        author = Item.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/buy/1')


# Test View
class CheckoutSessionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание 3 item для tests
        number_of_item = 3
        for item_num in range(number_of_item):
            Item.objects.create(first_name='first %s' % item_num, description='ffff %s' % item_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/buy/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('item/<int:id>/'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'checkout.html')

