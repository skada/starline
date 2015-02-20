from django.db import models
from django.utils.translation import ugettext_lazy as _

from people.models import Kid
from resources.models import Compound, Resource, ResourceBase


class BatchManager(models.Manager):

    def all_years(self):
        data = self.dates('start', 'year').distinct().defer('start')
        return data


class Batch(models.Model):
    BCH_PLANNING = 0
    BCH_READY = 1
    BCH_IN_PROGRESS = 2
    BCH_CLOSED = 3

    BATCH_STATE = (
        (BCH_PLANNING, _('Planning')),
        (BCH_READY, _('Ready')),
        (BCH_IN_PROGRESS, _('In progress')),
        (BCH_CLOSED, _('Closed')),
    )

    BATCH_STATE_DICT = dict(BATCH_STATE)

    objects = BatchManager()

    start = models.DateField(_('Start'))
    end = models.DateField(_('End'))
    compound = models.ForeignKey(Compound)
    state = models.PositiveSmallIntegerField(_('State'), choices=BATCH_STATE, default=BCH_PLANNING)

    def __str__(self):
        return '%s - %s - %s' % (self.compound, self.start, self.end)

    class Meta:
        verbose_name = _('Batch')
        verbose_name_plural = _('Batches')


class PlacementManager(models.Manager):

    def kids(self, batch):
        return self.filter(batch=batch, kid__isnull=False)

    def kids_by_group(self, batch, group):
        # TODO: implement
        return self.kids(batch)

    def kids_by_class(self, batch, klass):
        # TODO: implement
        return self.kids(batch)

    def kids_by_school(self, batch, school):
        # TODO: implement
        return self.kids(batch)


class Placement(models.Model):
    compound = models.ForeignKey(Compound, null=True, blank=True, related_name='compound')
    resource = models.ForeignKey(Resource)
    batch = models.ForeignKey(Batch)
    kid = models.ForeignKey(Kid, null=True, blank=True)

    objects = PlacementManager()

    def save(self, *args, **kwargs):
        root = self.resource.get_root()
        self.compound = Compound.objects.get(pk=root.id)
        super(Placement, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.batch, self.kid)

    class Meta:
        verbose_name = _('Placement')
        verbose_name_plural = _('Placements')