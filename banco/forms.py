from django import forms


from .models import Banco

class BancoForm(forms.ModelForm):

    class Meta:
        model = Banco
        fields = ('banco','ag','cc','gerente','contato','tel','email','obs')  