from django import forms
from account.models import Account
from track.models import Track


class CreateTrainee(forms.Form):
    first_name = forms.CharField(
        required=True,
        max_length=100,
        label="First Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your first name", "class": "form-control"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        max_length=100,
        label="Last Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your last name", "class": "form-control"}
        ),
    )
    date_of_birth = forms.DateField(
        required=True,
        label="Date of Birth",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )
    # account_obj = forms.ChoiceField(
    #     choices=Account.getall(),
    #     required=False,
    #     label="Account Username",
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )
    # track_obj = forms.ChoiceField(
    #     choices=Track.getall(),
    #     required=False,
    #     label="Track Name",
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )
    account_obj = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        required=True,
        label="Account",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    track_obj = forms.ModelChoiceField(
        queryset=Track.objects.all(),
        required=True,
        label="Track",
        widget=forms.Select(attrs={"class": "form-control"}),
    )


class UpdateTrainee(forms.Form):
    first_name = forms.CharField(
        required=True,
        max_length=100,
        label="First Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your first name", "class": "form-control"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        max_length=100,
        label="Last Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your last name", "class": "form-control"}
        ),
    )
    date_of_birth = forms.DateField(
        required=True,
        label="Date of Birth",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )
    account_obj = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        required=True,
        label="Account",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    track_obj = forms.ModelChoiceField(
        queryset=Track.objects.all(),
        required=True,
        label="Track",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
