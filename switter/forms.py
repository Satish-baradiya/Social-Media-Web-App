from logging import PlaceHolder
from pyexpat import model
from django import forms
from numpy import require
from .models import Sweet


class SweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "Placeholder":"Sweet something.....",
                "class":"textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Sweet
        exclude = ("user",)
