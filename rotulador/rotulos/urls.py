from django.urls import path
from .views import  RotuladorView

rotulos_urlpatterns = ([
    path('rotulos/', RotuladorView.as_view(), name='rotulos'),

], 'rotulos')
