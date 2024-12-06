from django import forms

from param.models import Centre




class CentreForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Centre

        # specify fields to be used
        fields = [
            "code",
            "nom",
            "description",
        ]