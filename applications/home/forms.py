from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        #fields = ("__all__")
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        wAidgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui'
               }
            )
        }
    

def clean_cantidad(self):
    cantidad = self.cleanned_data['cantidad']
    if cantidad < 10:
        raise forms.ValidationError('El numero ingresao debe ser mayor a 10')
    
    return cantidad