from django.views.generic import TemplateView, CreateView, UpdateView


class HomeView(TemplateView):
    template_name = 'page/home.html'




