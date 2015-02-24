from decimal import Decimal as D

from django.db import models
from django.utils.text import slugify
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


class Slugified(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Slugified, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AddressMixInModel(object):
    street1 = models.CharField(_('Street 1'), max_length=255, null=True, blank=True)
    street2 = models.CharField(_('Street 2'), max_length=255, null=True, blank=True)
    city = models.CharField(_('City'), max_length=100, null=True, blank=True)
    post_code = models.CharField(_('Post code'), max_length=10, null=True, blank=True)


class PositionMixIn(models.Model):
    left = models.IntegerField(_('Left'), default=10)
    top = models.IntegerField(_('Top'), default=10)

    class Meta:
        abstract = True