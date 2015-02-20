__author__ = 'skada'
from django import forms

from planning.models import Placement, Compound, Batch

import django_filters


class PlacementFilter(django_filters.FilterSet):
    class Meta:
        model = Placement
        fields = ['compound', 'batch',]
