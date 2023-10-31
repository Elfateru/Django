from django import forms

from myauth.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "bio", "avatar"
        # fields = "user", "bio", "avatar"

    # images = forms.ImageField(
    #     widget=forms.ClearableFileInput(attrs={"multiple": True}),
    #     required=False)
