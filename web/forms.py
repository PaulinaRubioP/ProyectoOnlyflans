# web/forms.py

from django import forms

from .models import Contact
class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo Electrónico',
            'message': 'Mensaje',
        }