from django import forms

class CepForm(forms.Form):
    cep = forms.CharField(label="CEP", max_length=9)