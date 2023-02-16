from .models import Rotulo
from .form import PageForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

class ProductCreate(CreateView):

    model = Rotulo
    form_class = PageForm

class RotuladorView(TemplateView):
    template_name = 'rotulos/rotulos.html'
