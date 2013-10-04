from django.db import models
from django import forms
#from bootstrap_toolkit import BootstrapTextInput

class AwsForm(forms.Form):

    AWS_KEY = forms.CharField(max_length=100,
                              required=True,
                             # widget=BootstrapTextInput(prepend='P')
    )
    AWS_SECRET = forms.CharField(max_length=100,
                                 required=True
    )