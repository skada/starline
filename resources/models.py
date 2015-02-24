from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from base.models import Slugified, PositionMixIn


class ResourceBase(MPTTModel, Slugified, PositionMixIn):
    parent = TreeForeignKey('self', null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = _('Resource Base')
        verbose_name_plural = _('Resources Bases')


class CompoundManager(models.Manager):

    def get_queryset(self):
        return super(CompoundManager, self).get_queryset().filter(parent__isnull=True)


class Compound(ResourceBase):
    objects = CompoundManager()

    class Meta:
        proxy = True


class ResourceManager(models.Manager):

    def get_queryset(self):
        return super(ResourceManager, self).get_queryset().filter(parent__isnull=False)


class Resource(ResourceBase):
    objects = ResourceManager()

    class Meta:
        proxy = True
