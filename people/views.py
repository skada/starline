from django.views.generic import CreateView, UpdateView

from people.forms import KidForm
from people.models import Kid

class KidCreate(CreateView):
    form_class = KidForm
    model = Kid

    def get_success_url(self):
        return self.request.GET.get('next')

class KidUpdate(UpdateView):
    form_class = KidForm
    model = Kid

    def get_success_url(self):
        return self.request.GET.get('next')
