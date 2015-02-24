from django.views.generic import CreateView, UpdateView, FormView

from people.forms import KidForm, EntryMedicalCheckFormSet
from people.models import Kid, EntryMedicalCheck


class KidCreate(CreateView):
    form_class = KidForm
    model = Kid

    def get_success_url(self):
        return self.request.GET.get('next')

class KidUpdate(UpdateView):
    form_class = KidForm
    model = Kid

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        entry_medical_check_formset = EntryMedicalCheckFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  entry_medical_check_form=entry_medical_check_formset,
                                  ))


    def get_success_url(self):
        return self.request.GET.get('next')


class EntryMedicalCheckFormSetView(FormView):
    form_class = EntryMedicalCheck
