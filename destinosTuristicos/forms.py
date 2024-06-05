from django import forms
from .models import *

class DestinoForm(forms.ModelForm):
    nombreCiudad = models.CharField(max_length = 100)
    imagenCiudad = models.ImageField(upload_to = 'pics')
    descripcionCiudad = models.TextField()
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField(default=False)

    class Meta:
        model = DestinosTuristicos
        fields = ['nombreCiudad', 'imagenCiudad', 'descripcionCiudad', 'precioTour', 'ofertaTour']

    def save(self, commit=True):
        destinos_turisticos = super().save(commit=False)
        if commit:
            destinos_turisticos.save()
        return destinos_turisticos