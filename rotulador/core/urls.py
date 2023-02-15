from django.urls import path
from .views import HomeView, RotuladorView, HistorialView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('historial/', HistorialView.as_view(), name='historial'),
]
