from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


class RotuladorView(TemplateView):
    template_name = 'core/rotulos.html'


class HistorialView(TemplateView):
    template_name = 'core/historial.html'
