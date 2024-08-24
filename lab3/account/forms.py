from django import forms

# id = models.AutoField(primary_key=True)
# username = models.CharField(max_length=100)
# password = models.CharField(max_length=200)
# email = models.EmailField()
# image = models.ImageField(upload_to="account/images/", blank=True, null=True)
# created_at = models.DateTimeField(auto_now_add=True)


class CreateAccount(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        required=True,
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "form-control"}
        ),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )


class UpdateAccount(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        required=False,
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "form-control"}
        ),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )
