from django import forms
from .models import GastoExtra

class GastoExtraForm(forms.ModelForm):
    class Meta:
        model = GastoExtra
        fields = ['descricao', 'valor']