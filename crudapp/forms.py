from django import forms
from . models import Detail

class detail_form(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'