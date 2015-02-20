from django.views.generic import TemplateView, FormView
from django_filters.views import FilterView

from planning.forms import PlacementFilter
from planning.models import Compound, Placement


class PlacementView(FilterView):
    filterset_class = PlacementFilter
    model = Placement

    def get_queryset(self):
        qs = super(PlacementView, self).get_queryset()
        compound_id = self.request.GET.get('compound')
        if compound_id:
            qs = qs.filter(compound__id=compound_id)
        return qs



