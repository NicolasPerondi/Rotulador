from django.views.generic.base import TemplateView


class RotuladorView(TemplateView):
    template_name = 'rotulos/rotulos.html'
