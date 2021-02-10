from django import forms

from .models import CentroDeCusto


class CentroDeCustoForm(forms.ModelForm):
    class Meta:
        model = CentroDeCusto
        fields = ('centroDeCusto',)