from decimal import Decimal as D

from django.test import TestCase

from base.models import Price


class PriceTest(TestCase):

    def setUp(self):
        pass

    def test_price_basics(self):
        p = Price(price=D("10.0"), tax_included=False, tax=D("0.21"))
        self.assertEqual(p.exc_tax, D("10.0"))
        self.assertEqual(p.inc_tax, D("12.1"))
        self.assertEqual(p.tax_amount, D("2.1"))
