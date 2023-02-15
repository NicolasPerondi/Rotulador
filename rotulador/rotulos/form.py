from django import forms
from rotulador.rotulos.models import Rotulo

class PageForm(forms.ModelForm):

    class Meta:
        model = Rotulo
        fields = ['codigo_Interno', 'n_Cajas', 'Zona_remitente']
        widgets ={
            'codigo_Interno' : forms.TextInput(attrs={'placeholder' : 'Codigo Interno' }),
            'n_Cajas': forms.Textarea(attrs={'placeholder': 'Numero de Cajas'}),
            'Zona_remitente': forms.TextInput(attrs={'placeholder': 'Zona que Despacha'}),
        }
        labels = {
            'Codigo Interno' : '', 'Nro de Cajas':'', 'Despacha': '',
        }
