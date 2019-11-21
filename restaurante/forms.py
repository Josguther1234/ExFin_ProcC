from django import forms
from .models import Menu, Plato,Carta

class CartaForm(forms.ModelForm):

    class Meta:
        model = Carta
        fields = ('menu','plato')

def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields["plato"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["plato"].help_text = "Ingrese los Actores que participaron en la película"
        self.fields["plato"].queryset = Plato.objects.all()
