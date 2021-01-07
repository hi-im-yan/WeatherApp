from django import forms


class Location(forms.Form):
    name = forms.CharField(max_length=100, label='Nome', widget=forms.TextInput(
        attrs={'placeholder': 'Cidade/Estado/Pais', 'class': 'form-control col-4'}))
