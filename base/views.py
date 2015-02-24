from django.views.generic import TemplateView, CreateView, UpdateView
from people.models import Kid
from resources.models import Compound


class HomeView(TemplateView):
    template_name = 'page/home.html'


class SchemaView(TemplateView):
    template_name = 'page/schema.html'

    def get_context_data(self, compound, **kwargs):
        context_data = super(SchemaView, self).get_context_data(**kwargs)

        compound = Compound.objects.get(slug=compound)
        resources = compound.get_leafnodes(False)
        context_data['resources'] = resources

        context_data['kids'] = Kid.objects.all()

        return context_data




