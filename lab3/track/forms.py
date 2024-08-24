from django import forms


class CreateTrack(forms.Form):
    # name = forms.CharField(required=True, max_length=100, label="Name")
    # description = forms.CharField(
    #     required=True, label="Description", widget=forms.Textarea
    # )
    # description = forms.CharField(required=True, label="Description")
    # image = forms.ImageField(required=False, label="Image")
    name = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your Description", "class": "form-control"}
        ),
    )
    description = forms.CharField(
        required=True,
        label="Description",
        widget=forms.Textarea(
            attrs={"placeholder": "Enter your Description", "class": "form-control"}
        ),
    )
    image = forms.ImageField(required=False, label="Image", widget=forms.FileInput())


class UpdateTrack(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your Name", "class": "form-control"}
        ),
    )
    description = forms.CharField(
        required=True,
        label="Description",
        widget=forms.Textarea(
            attrs={"placeholder": "Enter your Description", "class": "form-control"}
        ),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(),
    )
