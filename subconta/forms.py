from django import forms


from .models import Subconta


class SubcontaForm(forms.ModelForm):

    class Meta:
        model = Subconta
        fields = ('conta', 'subconta') 