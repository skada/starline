from decimal import Decimal as D

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Price(models.Model):
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    tax = models.DecimalField(_('Tax'), max_digits=3, decimal_places=2)
    tax_included = models.BooleanField(_('Tax included'), default=True)

    @property
    def inc_tax(self):
        if self.tax_included:
            return self.price
        else:
            return self.price * (D('1') + self.tax)

    @property
    def exc_tax(self):
        if self.tax_included:
            return self.price / (D('1') + self.tax)
        else:
            return self.price

    @property
    def tax_amount(self):
        return self.inc_tax - self.exc_tax

    class Meta:
        abstract = True


