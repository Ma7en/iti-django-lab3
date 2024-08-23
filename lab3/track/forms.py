from django import forms


class CreateTrack(forms.Form):
    name = forms.CharField(required=True, max_length=100, label="Name")
    # description = forms.CharField(
    #     required=True, label="Description", widget=forms.Textarea
    # )
    description = forms.CharField(required=True, label="Description")
    image = forms.ImageField(required=False, label="Image")
