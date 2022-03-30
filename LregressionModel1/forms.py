from django import forms
from django.forms import fields


class newForm(forms.Form):

    AGE = forms.FloatField(

        label='AGE', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'AGE', 'id': 'form-AGE'}))

    TSH = forms.FloatField(


        label='TSH',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'TSH', 'id': 'form-TSG'}),


    )

    T3 = forms.FloatField(

        label='T3', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'T3', 'id': 'form-T3'}))

    TT4 = forms.FloatField(

        label='TT4', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'TT4', 'id': 'form-TT4'}))

    T4U = forms.FloatField(

        label='T4U', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'T4U', 'id': 'form-T4U'}))

    FTI = forms.FloatField(

        label='FTI', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'FTI', 'id': 'form-FTI'}))

    choices = (
        (1, 'Surgery (Yes)'),
        (0, 'Surgery (No)'),
    )
    SURGERY = forms.ChoiceField(choices=choices, widget=forms.Select(
        attrs={'class': 'form-control mb-3', 'id': 'form_SURGERY'}))
    choices = (
        (1, 'Male'),
        (0, 'Female')
    )
    SEX = forms.ChoiceField(choices=choices, widget=forms.Select(
        attrs={'class': 'form-control mb-3', 'id': 'form_SEX'}))

    class Meta:
        fields = {'GREScore'}
