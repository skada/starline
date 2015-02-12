from django.db import models
from django.utils.translation import ugettext_lazy as _


class ResourceBase(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, db_index=True)


    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')


class CompoundManager(models.Manager):

    def get_queryset(self):
        return super(CompoundManager, self).get_queryset().filter(parent_isnull=True)


class Compound(ResourceBase):
    objects = CompoundManager()

    class Meta:
        proxy = True


class ResourceManager(models.Manager):

    def get_queryset(self):
        return super(CompoundManager, self).get_queryset().filter(parent_isnull=False)


class Resource(ResourceBase):

    class Meta:
        proxy = True
